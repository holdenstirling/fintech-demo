import sqlite3
import json
import os
from contextlib import contextmanager
from app.config import DATABASE_URL

DB_PATH = os.environ.get("DATABASE_URL", DATABASE_URL)


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                id          TEXT PRIMARY KEY,
                amount      INTEGER NOT NULL,
                currency    TEXT NOT NULL DEFAULT 'usd',
                customer_id TEXT NOT NULL,
                status      TEXT NOT NULL DEFAULT 'succeeded',
                description TEXT,
                processor_id TEXT,
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS idempotency_keys (
                idempotency_key  TEXT PRIMARY KEY,
                payment_response TEXT NOT NULL,
                created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_idempotency_created
            ON idempotency_keys(created_at)
        """)
        existing = conn.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
        if existing == 0:
            _seed_demo_data(conn)


def get_idempotency_result(key: str):
    """Return cached payment response for key if it exists and hasn't expired."""
    with get_connection() as conn:
        row = conn.execute(
            """SELECT payment_response FROM idempotency_keys
               WHERE idempotency_key = ?
               AND created_at > datetime('now', '-24 hours')""",
            (key,),
        ).fetchone()
    return json.loads(row["payment_response"]) if row else None


def store_idempotency_result(key: str, response_data: dict):
    """Persist an idempotency key → response mapping."""
    with get_connection() as conn:
        conn.execute(
            """INSERT OR REPLACE INTO idempotency_keys (idempotency_key, payment_response)
               VALUES (?, ?)""",
            (key, json.dumps(response_data)),
        )


def _seed_demo_data(conn):
    import uuid
    from datetime import datetime, timedelta
    import random

    customers = ["cust_A1B2", "cust_C3D4", "cust_E5F6", "cust_G7H8", "cust_J9K0"]
    descriptions = [
        "Monthly subscription",
        "One-time purchase",
        "Premium upgrade",
        "Invoice #8821",
        "Service fee",
    ]
    for i in range(12):
        ts = datetime.utcnow() - timedelta(hours=random.randint(1, 48))
        conn.execute(
            """INSERT INTO payments (id, amount, currency, customer_id, status, description, processor_id, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                str(uuid.uuid4()),
                random.choice([999, 1999, 4999, 9900, 19900]),
                "usd",
                random.choice(customers),
                "succeeded",
                random.choice(descriptions),
                f"proc_{uuid.uuid4().hex[:16]}",
                ts.strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

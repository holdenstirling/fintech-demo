import sqlite3
import os
from contextlib import contextmanager
from app.config import DATABASE_URL

_raw_path = os.environ.get("DATABASE_URL", DATABASE_URL)
# Resolve relative paths against the project root (parent of this file's directory)
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = _raw_path if os.path.isabs(_raw_path) else os.path.join(_project_root, _raw_path)


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
                key        TEXT PRIMARY KEY,
                payment_id TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Seed some realistic-looking data for the demo
        existing = conn.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
        if existing == 0:
            _seed_demo_data(conn)


def _seed_demo_data(conn):
    import uuid
    from datetime import datetime, timedelta

    # Fixed seed data — realistic mix of customers, amounts, currencies, and statuses.
    # Deterministic so the dashboard looks the same every demo run.
    records = [
        # (hours_ago, amount_cents, currency, customer_id, status, description)
        (1,   9900,  "usd", "cust_A1B2", "succeeded", "Monthly subscription — Pro plan"),
        (2,   4999,  "usd", "cust_E5F6", "succeeded", "Invoice #9204"),
        (3,   19900, "usd", "cust_C3D4", "succeeded", "Annual subscription renewal"),
        (4,   1499,  "eur", "cust_G7H8", "succeeded", "Invoice #9187"),
        (5,   9900,  "usd", "cust_J9K0", "succeeded", "Monthly subscription — Pro plan"),
        (6,   74900, "usd", "cust_A1B2", "succeeded", "Enterprise license Q2"),
        (7,   999,   "usd", "cust_C3D4", "failed",    "Invoice #9201 — card declined"),
        (9,   4999,  "usd", "cust_E5F6", "succeeded", "Seat expansion — 5 users"),
        (11,  2999,  "gbp", "cust_G7H8", "succeeded", "Wire transfer fee"),
        (13,  9900,  "usd", "cust_J9K0", "succeeded", "Monthly subscription — Pro plan"),
        (15,  19900, "usd", "cust_A1B2", "succeeded", "Invoice #9156"),
        (18,  1499,  "eur", "cust_C3D4", "succeeded", "Invoice #9144"),
        (20,  49900, "usd", "cust_E5F6", "succeeded", "Professional services — April"),
        (22,  9900,  "usd", "cust_G7H8", "failed",    "Monthly subscription — payment retry"),
        (24,  999,   "usd", "cust_J9K0", "succeeded", "Starter plan upgrade"),
        (28,  9900,  "usd", "cust_A1B2", "succeeded", "Monthly subscription — Pro plan"),
        (31,  4999,  "usd", "cust_C3D4", "succeeded", "Invoice #9133"),
        (35,  14900, "gbp", "cust_E5F6", "succeeded", "Invoice #9129"),
        (38,  9900,  "usd", "cust_G7H8", "succeeded", "Monthly subscription — Pro plan"),
        (42,  2499,  "usd", "cust_J9K0", "succeeded", "Add-on: advanced analytics"),
        (46,  74900, "usd", "cust_A1B2", "succeeded", "Enterprise license Q1"),
        (50,  9900,  "eur", "cust_C3D4", "succeeded", "Monthly subscription — Pro plan"),
        (55,  4999,  "usd", "cust_E5F6", "succeeded", "Invoice #9108"),
        (60,  1999,  "usd", "cust_G7H8", "succeeded", "Overage charge — API calls"),
        (68,  9900,  "usd", "cust_J9K0", "succeeded", "Monthly subscription — Pro plan"),
    ]

    now = datetime.utcnow()
    for hours_ago, amount, currency, customer, status, description in records:
        ts = now - timedelta(hours=hours_ago)
        conn.execute(
            """INSERT INTO payments
               (id, amount, currency, customer_id, status, description, processor_id, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                str(uuid.uuid4()),
                amount,
                currency,
                customer,
                status,
                description,
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

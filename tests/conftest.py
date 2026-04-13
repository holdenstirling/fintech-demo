import pytest
import app.database as db_module
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def isolated_db(tmp_path, monkeypatch):
    db_path = str(tmp_path / "test.db")
    monkeypatch.setattr(db_module, "DB_PATH", db_path)
    db_module.init_db()
    yield


@pytest.fixture
def client(isolated_db):
    from app.main import app
    with TestClient(app) as c:
        yield c

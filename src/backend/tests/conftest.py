import pytest
from starlette.testclient import TestClient

from app import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here

# openid profile User.Read email

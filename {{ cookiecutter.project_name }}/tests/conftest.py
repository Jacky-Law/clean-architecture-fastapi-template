import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from {{cookiecutter.service_name}}.entrypoints.fastapi_app import app


@pytest.fixture(scope="function")
async def async_api_client():
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c


@pytest.fixture(scope="function")
def api_client():
    with TestClient(app=app, base_url="http://test") as c:
        yield c

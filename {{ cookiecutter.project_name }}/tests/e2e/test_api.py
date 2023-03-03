import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_async(async_api_client: AsyncClient):

    resp = await async_api_client.get("/")

    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World"}


def test_root(api_client: TestClient):

    resp = api_client.get("/")

    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World"}

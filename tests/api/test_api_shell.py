from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

EXPECTED_PATHS = {
    "/api/v1/health",
    "/api/v1/auth/register",
    "/api/v1/auth/login",
    "/api/v1/me",
    "/api/v1/assets/search",
    "/api/v1/assets/{symbol}/latest",
    "/api/v1/watchlists",
    "/api/v1/watchlists/{watchlist_id}/items",
    "/api/v1/watchlists/{watchlist_id}/items/{asset_id}",
    "/api/v1/alerts",
    "/api/v1/alerts/{alert_id}",
    "/api/v1/alert-events",
}


def test_health_endpoints_work() -> None:
    expected = {
        "status": "ok",
        "service": "market-watch-api",
        "environment": "dev",
    }

    assert client.get("/health").json() == expected
    assert client.get("/api/v1/health").json() == expected


def test_openapi_contains_expected_api_shell_paths() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200

    paths = set(response.json()["paths"].keys())
    assert EXPECTED_PATHS.issubset(paths)


def test_stubbed_route_returns_consistent_501_response() -> None:
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "user@example.com", "password": "password123"},
    )

    assert response.status_code == 501
    assert response.json() == {
        "error": "not_implemented",
        "message": "POST /api/v1/auth/register is part of the Step 6 API shell and will be implemented in a later step.",
    }
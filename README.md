# market-watch-api

Backend-first Market Watch & Alerts API for personal watchlists and finance research workflows.

## Current status

This repo is currently at **Step 6: API shell**.

In place now:

- Docker Compose local stack:
  - `api`
  - `db`
  - `worker`
- SQLAlchemy 2.0 ORM models for the V1 schema
- Alembic migration chain:
  - `0001_step3_bootstrap`
  - `0002_step4_create_v1_schema`
- versioned API routing under `/api/v1`
- thin route handlers
- typed request and response schemas
- service-layer stubs for unfinished business logic
- legacy `GET /health` kept working for backwards compatibility
- canonical versioned `GET /api/v1/health`

## V1 boundaries

Locked in `PROJECT_SCOPE.md`:

- assets: stocks and ETFs only
- alert types:
  - `price_above`
  - `price_below`
  - `pct_move_up_1d`
  - `pct_move_down_1d`
- market data cadence: every 15 minutes during US market hours on trading days
- deployment target: Render

## Local quickstart

### 1. Create your local env file

```bash
cp .env.example .env
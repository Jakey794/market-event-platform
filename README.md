# market-watch-api

Backend-first Market Watch & Alerts API for personal watchlists and finance research workflows.

## Current status

This repo is currently at **Step 3: local containers**.

In place now:

- FastAPI application entrypoint
- env-based configuration
- SQLAlchemy database scaffold
- `GET /health` endpoint
- local Docker Compose stack with:
  - `api`
  - `db`
  - `worker`
- Alembic bootstrap so migration commands run locally

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
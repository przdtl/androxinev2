#!/bin/sh

sh ./scripts/alembic.sh

fastapi run ./src/main.py --reload

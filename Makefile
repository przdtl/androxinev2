# Development
.PHONY: dev-up
dev-up:
	docker compose --env-file .env.dev -f docker-compose.dev.yml up --build -d
	docker compose --env-file .env.dev -f docker-compose.dev.yml logs -f

.PHONY: dev-down
dev-down:
	docker compose --env-file .env.dev -f docker-compose.dev.yml down

.PHONY: dev-logs
dev-logs: 
	docker compose --env-file .env.dev -f docker-compose.dev.yml logs -f


# Testing
.PHONY: test-up
test-up:
	docker compose --env-file .env.test -f docker-compose.test.yml up --build -d
	docker compose --env-file .env.test -f docker-compose.test.yml logs -f

.PHONY: test-down
test-down:
	docker compose --env-file .env.test -f docker-compose.test.yml down

.PHONY: test-logs
test-logs: 
	docker compose --env-file .env.test -f docker-compose.test.yml logs -f

.PHONY: lint
lint: 
	uv run ruff check .
	uv run mypy app


# Production
.PHONY: prod-up
prod-up:
	docker compose --env-file .env.prod -f docker-compose.prod.yml up --build -d

.PHONY: prod-down
prod-down:
	docker compose --env-file .env.prod -f docker-compose.prod.yml down

.PHONY: prod-logs
prod-logs: 
	docker compose --env-file .env.prod -f docker-compose.prod.yml logs -f

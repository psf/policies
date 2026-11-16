.DEFAULT_GOAL := help

SITE_DIR ?= site

help: ## Display this help text
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development

serve: ## Start the live-reloading docs server on http://localhost:10000
	docker compose up --build

build: ## Build the site into ./site (or SITE_DIR=...)
	uv run mkdocs build --clean --site-dir "$(SITE_DIR)"

clean: ## Stop the docs server and remove the built site
	docker compose down
	rm -rf "$(SITE_DIR)"

##@ Code Quality

lint: ## Run ruff linter (--fix enabled)
	uv run ruff check --fix

fmt: ## Format Python and pyproject.toml
	uv run ruff format
	@uv run pyproject-fmt pyproject.toml || uv run pyproject-fmt --check pyproject.toml

typecheck: ## Run ty type checker
	uv run ty check

check: ## Check lint, formatting and types without changing files
	uv run ruff check
	uv run ruff format --check
	uv run pyproject-fmt --check pyproject.toml
	uv run ty check

ci: lint fmt typecheck build ## Run lint, fmt, typecheck, then build

.PHONY: help serve build clean
.PHONY: lint fmt typecheck check ci

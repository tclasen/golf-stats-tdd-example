FILES := $(shell find src tests -name "*.py")
VENV := .venv
VENVTOUCHFILE := $(VENV)/touchfile
LINTTOUCHFILE := $(VENV)/lint-touchfile
TESTTOUCHFILE := $(VENV)/test-touchfile
HOOKTOUCHFILE := .git/hooks/touchfile

##############################
########## Primary Tasks
##############################

.PHONY: help
help: ## Display this help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: lint test ## Run all common development tasks

.PHONY: install
install: $(VENVTOUCHFILE) ## Install development environment tooling

.PHONY: lint
lint: $(LINTTOUCHFILE) ## Run linters

.PHONY: test
test: $(TESTTOUCHFILE) ## Run tests

.PHONY: clean
clean: ## Clean working environment
	git clean -dfX

##############################
########## Secondary Tasks
##############################

$(VENVTOUCHFILE): poetry.lock
	poetry install --remove-untracked --no-interaction
	@touch $@

poetry.lock: pyproject.toml
	poetry lock --no-update --no-interaction
	@touch $@

$(HOOKTOUCHFILE): $(VENVTOUCHFILE) .pre-commit-config.yaml
	poetry run pre-commit install --install-hooks -t pre-commit -t commit-msg
	@touch $@

$(LINTTOUCHFILE): $(FILES) $(HOOKTOUCHFILE)
	poetry run mypy .
	poetry run pflake8
	poetry run black .
	poetry run isort .
	poetry run toml-sort pyproject.toml --check || poetry run toml-sort pyproject.toml
	@touch $@

$(TESTTOUCHFILE): $(FILES) $(VENVTOUCHFILE)
	poetry run pytest
	@touch $@
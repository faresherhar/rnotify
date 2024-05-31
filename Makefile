# Docker
ARTIFACTORY_URL="localhost"

IMAGE_NAME="username/rnotify-app"
IMAGE_TAG="v0.0.1"
IMAGE=${ARTIFACTORY_URL}/${IMAGE_NAME}:${IMAGE_TAG}

.PHONY: build_src
build_src:
	@podman build --tag ${IMAGE} --file Dockerfile ./

.PHONY: publish_src
publish_src: build_src
	@podman push ${IMAGE}

.PHONY: debug_src
debug_src:
	@podman run --rm -ti ${IMAGE} /bin/sh

# Run commands
.PHONY: init_db
init_db:
	@python src/init_db.py

.PHONY: run_scraper
run_scraper:
	@python src/main.py scrap

.PHONY: run_notifier
run_notifier:
	@python src/main.py notify

.PHONY: run_cleaner
run_cleaner:
	@python src/main.py clean

.PHONY: run_asgi
run_asgi:
	@uvicorn --reload --app-dir ${PWD}/src/ asgi:app --host 0.0.0.0 --port 8080

.PHONY: run_tests
run_tests:
	@pytest
	@rm test.db

# Setup commands
.PHONY: setup
setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

.PHONY: clean
clean:
	@find -name '*__pycache__' | xargs rm -rf
	# @rm -rf .env *.db .config/ .pytest_cache/ .venv/

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
.PHONY: run_scraper
run_scraper:
	@python src/scraper.py

.PHONY: run_notifier
run_notifier:
	@python src/notifier.py


# Setup commands
.PHONY: setup
setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

.PHONY: clean
clean:
	@find -name '*__pycache__' | xargs rm -rf
	@rm -rf .pytest_cache/ .venv/

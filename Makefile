# Docker
ARTIFACTORY_URL="localhost"

IMAGE_NAME="username/rnotify"
IMAGE_TAG="v0.0.1"
IMAGE=${ARTIFACTORY_URL}/${IMAGE_NAME}:${IMAGE_TAG}

.PHONY: build_src
build_src:
	@podman build --tag ${IMAGE} --file Dockerfile ./

.PHONY: publish_src
publish_src: build_src
	@podman push ${IMAGE}


# Start Application
.PHONY: run
run:
	@python src/main.py


# Setup commands
.PHONY: setup
setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

.PHONY: clean
clean:
	@find -name '*__pycache__' | xargs rm -rf
	@rm -rf .pytest_cache/ .venv/

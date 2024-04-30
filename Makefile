# Docker images
ARTIFACTORY_URL="localhost"

SRC_IMAGE_NAME="username/rnotify-app"
SRC_IMAGE_TAG="v0.0.1"
SRC_IMAGE=${ARTIFACTORY_URL}/${SRC_IMAGE_NAME}:${SRC_IMAGE_TAG}

DASHBOARD_IMAGE_NAME="username/rnotify-dashboard"
DASHBOARD_IMAGE_TAG="v0.0.1"
DASHBOARD_IMAGE=${ARTIFACTORY_URL}/${DASHBOARD_IMAGE_NAME}:${DASHBOARD_IMAGE_TAG}

## Rnotify App Image
.PHONY: build_src
build_src:
	@docker build --tag ${SRC_IMAGE} --file docker/src/Dockerfile ./

.PHONY: publish_src
publish_src: build_src
	@docker push ${SRC_IMAGE}

## Rnotify Dashboard Image
.PHONY: build_dashboard
build_dashboard:
	@docker build --tag ${DASHBOARD_IMAGE} --file docker/dashboard/Dockerfile ./

.PHONY: publish_dashboard
publish_dashboard: build_dashboard
	@docker push ${DASHBOARD_IMAGE}


# Run commands
.PHONY: run_scraper
run_scraper:
	@python src/scraper.py

.PHONY: run_notifier
run_notifier:
	@python src/notifier.py

.PHONY: run_cleaner
run_cleaner:
	@python src/cleaner.py

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
	@rm -rf .env *.db .config/ .pytest_cache/ .venv/

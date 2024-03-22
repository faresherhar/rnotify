setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

clean:
	@find -name '*__pycache__' | xargs rm -rf
	@rm -rf .env *.db .config/ .pytest_cache/ .venv/


run_scraper:
	@python src/scraper.py

run_notifier:
	@python src/notifier.py

run_cleaner:
	@python src/cleaner.py

run_asgi:
	@hypercorn --reload --bind 0.0.0.0:8000 src/asgi:app

run_tests:
	@pytest
	@rm test.db
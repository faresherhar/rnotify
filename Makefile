setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

test:
	@pytest

clean:
	@find -name '*__pycache__' | xargs rm -rf


run_scraper:
	@python src/main.py
setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

load_env:
	@export $(grep -v '^#' .env | xargs)

clean:
	@find -name '*__pycache__' | xargs rm -rf


run_scraper:
	@python src/scraper.py
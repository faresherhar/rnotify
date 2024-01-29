setup:
	@find . -wholename "./requirements/*.txt" -type f -exec pip install -r '{}' ';'

clean:
	@find -name '*__pycache__' | xargs rm -rf


run_scraper:
	@python src/scraper.py
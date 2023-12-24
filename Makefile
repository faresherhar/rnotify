setup:
	@pip install -r requirements.txt
	@pip install black

test:
	@pytest

clean:
	@find -name '*__pycache__' | xargs rm -rf

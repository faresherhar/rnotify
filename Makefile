setup:
	@pip install -r requirements.txt
	@pip install black

clean:
	@find -name '*__pycache__' | xargs rm -rf
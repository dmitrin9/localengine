.PHONY: run test

run:
	FLASK_ENV=development
	flask --app app run

test:
	python test.py

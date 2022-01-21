.PHONY: run fmt

run:
	./venv/bin/python fossclub/manage.py runserver

fmt:
	./venv/bin/python -m black fossclub/

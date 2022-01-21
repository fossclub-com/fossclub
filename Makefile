.PHONY: run fmt all-migrate make-mgrt mgrt

# include .env vars
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

run:
	./venv/bin/python fossclub/manage.py runserver

fmt:
	./venv/bin/python -m black fossclub/

all-migrate: make-mgrt mgrt

make-mgrt:
	./venv/bin/python fossclub/manage.py makemigrations

mgrt:
	./venv/bin/python fossclub/manage.py migrate

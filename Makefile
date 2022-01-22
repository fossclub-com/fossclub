.PHONY: run fmt all-migrate make-mgrt mgrt setup python-setup pip superuser

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

python-setup: pip

pip: venv
	./venv/bin/python -m pip install -r requirements.txt

venv:
	python3 -m venv venv

superuser:
	./venv/bin/python fossclub/manage.py createsuperuser

shell:
	./venv/bin/python fossclub/manage.py shell

huey:
	./venv/bin/python fossclub/manage.py run_huey

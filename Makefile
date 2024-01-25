SHELL := /bin/bash

LOCALES_DIR := locales
POT_FILE := $(LOCALES_DIR)/messages.pot
LANG := uk

f = docker-compose.yml

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null

build:
	docker-compose -f $(f) build

up:
	docker-compose -f $(f) up -d

down:
	docker-compose -f $(f) down

drm:
	docker-compose -f $(f) down -v --remove-orphans

lg:
	docker-compose -f $(f) logs -f

bup: build up

bupl: build up lg

dbup: down bup

dbupl: down bupl

ps:
	docker ps -a

sh:
	docker-compose -f $(f) exec app bash

mkm:
	docker-compose -f $(f) exec app alembic revision --autogenerate

mg:
	docker-compose -f $(f) exec app alembic upgrade head

shmg:
	docker-compose -f $(f) exec app python manage.py showmigrations

admin:
	docker-compose -f $(f) exec app python manage.py createsuperuser --username admin

dump:
	docker-compose -f $(f) exec app python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.permission --indent 2 > services/backend/service/dump.json

load:
	docker-compose -f $(f) exec app python manage.py loaddata dump.json

init-messages:
	docker-compose -f $(f) exec app pybabel extract -F babel.cfg -o $(POT_FILE) .
update-messages: init-messages
init-language:
	docker-compose -f $(f) exec app pybabel init -i $(POT_FILE) -d $(LOCALES_DIR) -l $(LANG)
update-language: init-language
compile-language:
	docker-compose -f $(f) exec app pybabel compile -d $(LOCALES_DIR)

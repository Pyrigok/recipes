
build:
	docker-compose -f docker-compose.yml build --no-cache

up:
	docker-compose -f docker-compose.yml up

down:
	docker-compose -f docker-compose.yml down

docker_migrations:
	docker exec -it recipes bash -c 'python recipes/recipes/manage.py makemigrations'

docker_migrate:
	docker exec -it recipes bash -c 'python recipes/recipes/manage.py migrate'

shell:
	docker exec -it recipes shell

bash:
	docker exec -it recipes bash

admin:
	docker exec -it recipes bash -c 'python recipes/recipes/manage.py createsuperuser'

static:
	docker exec -it recipes bash -c 'python recipes/recipes/manage.py collectstatic --noinput'

dump:
	python3 recipes/recipes/manage.py dumpdata --indent=4 > recipes_backup.json

loaddata:
	docker exec -it recipes bash -c "python3 recipes/recipes/manage.py loaddata recipes_app_backup.json"

run:
	python3 recipes/recipes/manage.py runserver

superuser:
	python3 recipes/recipes/manage.py createsuperuser

migrations:
	python recipes/recipes/manage.py makemigrations

migrate:
	python recipes/recipes/manage.py migrate

active:
	source recipes_venv/bin/activate

# create and populate the Elasticsearch index and mapping
index:
	python recipes/recipes/manage.py search_index --rebuild


# init css for django with tailwind
css:
	python recipes/recipes/manage.py tailwind init

css_start:
	python recipes/recipes/manage.py tailwind start

# init css for django with tailwind
css_install:
	python recipes/recipes/manage.py tailwind install

# train chatter bot
train:
	python recipes/recipes/manage.py train

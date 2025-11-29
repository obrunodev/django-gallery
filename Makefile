run:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

createsuperuser:
	poetry run python manage.py createsuperuser

collectstatic:
	poetry run python manage.py collectstatic

startapp:
	poetry run python manage.py startapp $(APP_NAME)

run-dev:
	python manage.py runserver

test:
	coverage run manage.py test
	coverage report

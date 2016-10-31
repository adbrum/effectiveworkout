all:
	pip install -r requirements-dev.txt
	./manage.py migrate
	./manage.py loaddata */config/fixtures/*.json
	./manage.py loaddata */exercises/fixtures/*.json
	./manage.py createsuperuser --email=''
	./manage.py runserver
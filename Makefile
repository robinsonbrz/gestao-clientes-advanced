default: 
	@echo "Comandos disponíveis "
	@echo "	make makemigrations  - cria migrations"
	@echo "	make migrate         - executa migrations"
	@echo "	make createsuperuser - criar um usuario"
	@echo "	make start           - inicializa container, e executa serviço Django"


makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser  
	# --username rob --email r@r.com 

start:
	python manage.py runserver 0.0.0.0:8000

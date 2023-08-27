default: 
	@echo "Comandos disponíveis "
	@echo "	make build           - cria containers caso não os tenha, ou caso modifique .env.dev"
	@echo "	make makemigrations  - cria migrations"
	@echo "	make migrate         - executa migrations"
	@echo "	make createsuperuser - criar um usuario"
	@echo "	make start           - inicializa container, e executa serviço Django"
	@echo "	make stop            - encerra execução dos containers BD e Django"

# build:
# 	docker-compose -f docker-compose-dev.yaml --env-file=.env.dev up -d --build

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser --username rob --email r@r.com 

start:
	python manage.py runserver 0.0.0.0:8000

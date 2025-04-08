
.PHONY: help run migrate createsuperuser test makemigrations logs restart

help:
	@echo "📘 Команды:"
	@echo "  make run                — запустить сервер"
	@echo "  make migrate            — применить миграции"
	@echo "  make makemigrations     — создать миграции"
	@echo "  make createsuperuser    — создать суперпользователя"
	@echo "  make test               — запустить тесты"
	@echo "  make logs               — посмотреть логи контейнера"
	@echo "  make restart            — перезапустить контейнер web"

run:
	docker-compose up --build -d

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

test:
	docker-compose exec web python manage.py test

logs:
	docker-compose logs -f web

restart:
	docker-compose restart web

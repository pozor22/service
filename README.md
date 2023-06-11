# service

Это тестовая API с тестовыми данными и моделями, предназначенная для демонстрации работы с инструментами:
Django, Docker, djangorestframework, celery, redis и postgresql

Все для запуска находится в контейнерах и для запуска нужно:
 Ввести команду из папки приложения:
  - docker-compose build
 
 А после запустить приложение:
  - docker-compose up
 
 Все отображаемые данные находятся по http://127.0.0.1:8000/api/subscriptions/?format=json и отображаются в json формате

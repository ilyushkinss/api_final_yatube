# Проект API для YaTube.

Позволяет делать GET, PUT, PATCH и DELTE запросы к социальной сети YaTube.

## Запуск проекта: 

### 1) Клонируем репозиторий:

https://github.com/ilyushkinss/api_final_yatube

### 2) Создаем и активируем виртуальное окружение:

python -m venv venv

source venv/Scripts/activate

### 3) Устанавливаем зависимости из requirements:

pip install -r requirements.txt

### 4) Применяем миграции:

python manage.py migrate

### 5) Запускаем проект:

python manage.py runserver



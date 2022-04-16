### Управление объявлениями
## Установка
#### нет времени?
запустите многовенно при помощи докера
```shell
docker-compose up
```

Откройте виртуальное окружение при помощи pipenv и скачайте зависимисти
```shell
pipenv shell
pipenv install
```

У вас должен быть установлен и запущен PostgreSQL

Задайте переменные окружения
```shell
SECRET_KEY=your_secret_key
DEBUG_MODE=True
DATABASE_URL=postgres://user:password@host:port/dbname
```
сделайте миграции и можно запускать
```shell
python manage.py migrate
python manage.py runserver
```
Откройте виртуальное окружение при помощи pipenv и скачайте зависимисти
```shell
pipenv shell
pipenv install
```

# Сервис Feedback
Сервис Feedback позволяет отправлять форму обратной связи.
Для того чтобы отправить форму обратной связи нужно быть зарегистрированным и авторизованным.
Так же форма отправляется одним пользователем 1 раз в сутки, для каждого пользователя.

# Ресурсы API Feedback
**AUTH**: аутентификация.

**USERS**: пользователи.

**Feedback**: сама форма обратной связи с возможностью прикреплять файлы.

**SWAGGER**: документация через которую удобно делать запросы.

# Алгоритм регистрации пользователей
Пользователь отправляет POST-запрос с параметром users http://127.0.0.1:8000/auth/users/ 
Для регистрации необходимо указать Адрес электронной почты, пароль и имя пользователя.
Далее необходимо получить токен на ваш выбор либо обычный Token либо JWT токен
Пользователь отправляет POST-запрос с параметрами http://127.0.0.1:8000/auth/token/login вводит имя пользователя и пароль для авторизации.
Пользователь отправляет POST-запрос с параметрами http://127.0.0.1:8000/auth/jwt/create вводит имя пользователя и пароль для авторизации.
Эти операции выполняются один раз, при регистрации пользователя. В результате пользователь получает токен и может работать с API

# Пользовательские роли

**Аутентифицированный пользователь (user)** — может отправить форму обратной связи только раз в сутки.
**Неавторизованный пользователь** - не сможет отправить форму обратной связи пока не авторизуется.
**Менеджер** - имеет полные права может зайти в админ панель и там будет вся необходимая информация для него.

# Установка
Склонируйте репозиторий. Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`, активируйте его (Windows: `source venv\scripts\activate`; Linux/Mac: `source venv/bin/activate`), установите зависимости `python -m pip install -r requirements.txt`.

Для запуска сервера разработки,  находясь в директории проекта выполните команды:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Проект запущен и доступен по адресу [localhost:8000](http://localhost:8000/).
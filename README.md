<h2>users-blogs-v2</h2>
Users blogs service Python 3.8, Django 3.0, SQLite3. Requirements.txt прилагается.<br> 
Для запуска проекта должен быть установлен docker (проект тестировался на версии 19.03.14)<br>
и docker-compose (проект тестировался на версии 1.27.4, build 40524192)<br>
Чтобы запустить проект перейдите в папку /users-blogs-v2/users_blogs_v2/ и используйте команду <br>
<br>
docker-compose up<br>
<br>
Стартовая страница проекта доступна по адресу http://localhost:8000/<br>
В систему заведены тестовые пользователи (login):<br>
admin - суперпользователь<br>
Vova<br>
Misha<br>
Dima<br>
Kolya<br>
Gena <br>
Все пароли одинаковые - "1".<br>
Регистрация новых аккаунтов сделана для удобства тестирования. Аккауны добавляются без электронной почты.<br>
Электронную почту к аккаунту можно добавить через админку.
Ввиду отсутствия в момент разработки настроенного SMTP-сервера почтовый бэкенд настроен на консоль:<br>
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' <br>
Вывод почтового клиента можно увидеть в терминале запуска docker-compose в строчках, относящихся к celery<br>
(сервис web1_1)<br>
web_1    | [10/Apr/2021 18:27:34] "POST /post_create/?csrfmiddlewaretoken=GFU1ixNo047aprihhIptavwu3YLguw88hGgTYugIr2Z1FJEzgBaiM6PIlveQT4L1 HTTP/1.1" 302 0<br>
web1_1   | [2021-04-10 18:27:34,915: INFO/MainProcess] Received task: ubservs.models.indef_task[c6b1c32a-eec1-4194-8131-fdd88ce83f0a]<br>
web_1    | [10/Apr/2021 18:27:34] "GET /post_list/ HTTP/1.1" 200 2390<br>
web1_1   | [2021-04-10 18:27:34,961: WARNING/ForkPoolWorker-1] Content-Type: text/plain; charset="utf-8"<br>
web1_1   | MIME-Version: 1.0<br>
web1_1   | Content-Transfer-Encoding: 7bit<br>
web1_1   | Subject: Add a new post in your News<br>
web1_1   | From: from@example.com<br>
web1_1   | To: test@test.com<br>
web1_1   | Date: Sat, 10 Apr 2021 15:27:34 -0000<br>
web1_1   | Message-ID: <161806845495.8.13845576515333582567@9a45c9ce9714><br>
web1_1   | <br>
web1_1   | Dear admin, user Gena add a new post. See it in the /news/<br>
web1_1   | [2021-04-10 18:27:34,961: WARNING/ForkPoolWorker-1] <br>-------------------------------------------------------------------------------<br>
web1_1   | [2021-04-10 18:27:34,996: INFO/ForkPoolWorker-1] Task ubservs.models.indef_task[<br>c6b1c32a-eec1-4194-8131-fdd88ce83f0a] succeeded in 0.0785509359993739s: None<br>

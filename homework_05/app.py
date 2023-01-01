"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask +
создайте index view / +
добавьте страницу /about/, добавьте туда текст +
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template) +
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их+
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)+
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for+
"""

# pytest testing/test_homework_05 -s -vv

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get("/", endpoint="home_page")
def hello_page():
    return render_template("hello.html")


@app.get("/about/", endpoint="about_page")
def about_page():
    return render_template("about.html")


@app.get("/buttons/")
def buttons_page():
    return render_template("buttons.html")


@app.get("/forms/")
def forms_page():
    return render_template("forms.html")


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import random
import string

app = Flask(__name__)

facts_list = ["Привет", "Пока", "Как дела?"]
mon = ['Орёл', 'Решка']


@app.route("/")
def hello_world():
    return '<h1>Тут ты можешь посмотреть рандомные факты</h1> <a href="/random_fact">Посмотреть случайный факт!</a> <a href="/monetka">Подбросить монетку</a> <a href="/generate_password">Сгенерировать пароль</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p> '

@app.route("/secret")
def secrets():
    return '<a>Секретная страница🤫</a>'

@app.route("/monetka")
def orel_or_reshca():
    return f'<p>{random.choice(mon)}</p>'

@app.route("/generate_password")
def passwords():
    return f'<p>{"".join(random.choices(string.ascii_letters + string.digits, k=12))}</p>'

app.run(debug=True)

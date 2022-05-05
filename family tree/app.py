# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    name = "Alex" # escreva seu nome
    age = "12" # escreva sua idade

    return render_template('index.html' , name = name , age = age)

# defina a rota para a página do pai
@app.route("/father")
def father():

    name = "Vítor" # escreva seu nome
    age = "40" # escreva sua idade

    return render_template('father.html' , name = name , age = age)

# defina a rota para a página da mãe
@app.route("/mother")
def mother():

    name = "Erica" # escreva seu nome
    age = "37" # escreva sua idade

    return render_template('mother.html' , name = name , age = age)


# definia a rota para a página do amigo
@app.route("/friend")
def friend():

    name = "Pedro" # escreva seu nome
    age = "12" # escreva sua idade

    return render_template('friend.html' , name = name , age = age)


# adicione outras rotas, se você quiser


# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/alunos')
def alunos():
    lista_alunos = [
        {"nome": "Alice", "matricula": "12345678"},
        {"nome": "Bruno", "matricula": "87654321"},
        {"nome": "Clara", "matricula": "11223344"},
        {"nome": "Marcos", "matricula": "55667788"},
    ]
    return render_template('alunos.html', alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ pizzpizzaria/<sabor>')
def pizzaria(sabor):
    if sabor == 'calabresa':
        return render_template('pizzaCalabresa.html')

    elif sabor == 'marguerita':
        return render_template('pizzaMarguerita.html')

    elif sabor ==  'frango':
        return render_template('pizzaFrango.html')

    else:
        return render_template('erro.html')

if __name__ == '__main__':
    app.run(debug=True)
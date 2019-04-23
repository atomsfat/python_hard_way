from flask import Flask
from flask import render_template  # Jinja2
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get('name', 'No-body')
    if name:
        greeting = f'hello {name}'
    else:
        greeting = 'hello world'
    return render_template('index.html', greeting=greeting)


@app.route('/hello', methods=['POST', 'GET'])
def hello_post():
    greeting = 'Hello Word'

    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet}, {name}'
        return render_template('index.html', greeting=greeting)
    else:
        return render_template('hello_form.html')


if __name__ == '__main__':
    app.run()

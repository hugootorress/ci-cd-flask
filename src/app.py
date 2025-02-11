from flask import Flask

PORT = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola mundo"

@app.route('/hugo')
def saludopersonal():
    return "Hola amigo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '✅ Conexión segura establecida con HTTPS'

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))

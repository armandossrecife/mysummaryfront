from flask import Flask, render_template, send_from_directory
import os 

app = Flask(__name__)
app.secret_key = "my_secret_key"

BACKEND_IP = os.getenv('BACKEND_IP')
BACKEND_PORT = os.getenv('BACKEND_PORT')
FASTAPI_URL = "http://localhost:8000"

STATIC_PATH = os.path.join(app.root_path, 'static')

if BACKEND_IP and BACKEND_PORT:
    FASTAPI_URL = f"http://{BACKEND_IP}:{BACKEND_PORT}"
else:
    print("Você precisa definir o IP e porta da aplicação backend")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(STATIC_PATH, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def inde():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/registro')
def registro():
    return render_template('auth/registro.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/principal.html')

@app.route('/processo')
def processo_selecionado():
    return render_template('processos/processo.html')
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
    info_dashboard = {
        'titulo':"Dashboar",
        'imagem':"static/assets/icons/person-circle.svg",
        'nome':"armando",
        'breadcrumb':"Dashboard Principal",
        'mensagem':"Esta é uma mensagem de feedback assim que o dashboard principal é carregado."
    }
    return render_template('dashboard/principal.html', titulo=info_dashboard['titulo'], imagem_profile=info_dashboard['imagem'],
    nome_usuario=info_dashboard['nome'], breadcrumb_item_active=info_dashboard['breadcrumb'], mensagem_feedback=info_dashboard['mensagem'])

@app.route('/processo')
def processo_selecionado():
    return render_template('processos/processo.html')

@app.route('/profile')
def edit_profile():
    info_dashboard = {
        'titulo':"Editar Profile",
        'imagem':"static/assets/icons/person-circle.svg",
        'nome':"armando",
        'breadcrumb':"Profile",
        'mensagem':"Esta é uma mensagem de feedback após edição do usuário."
    }

    return render_template('dashboard/profile.html', titulo=info_dashboard['titulo'], imagem_profile=info_dashboard['imagem'],
    nome_usuario=info_dashboard['nome'], breadcrumb_item_active=info_dashboard['breadcrumb'], mensagem_feedback=info_dashboard['mensagem'])

@app.route('/password')
def edit_passoword():
    info_dashboard = {
        'titulo':"Editar Password",
        'imagem':"static/assets/icons/person-circle.svg",
        'nome':"armando",
        'breadcrumb':"Password",
        'mensagem':"Esta é uma mensagem de feedback após edição do password do usuário."
    }
    return render_template('dashboard/password.html', titulo=info_dashboard['titulo'], imagem_profile=info_dashboard['imagem'],
    nome_usuario=info_dashboard['nome'], breadcrumb_item_active=info_dashboard['breadcrumb'], mensagem_feedback=info_dashboard['mensagem'])
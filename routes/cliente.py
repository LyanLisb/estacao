from flask import Blueprint, render_template, request


client_route = Blueprint('client',__name__)


@client_route.route('/')
def historico_geral():
    return render_template('historicogeral.html')

@client_route.route('/temperatura')
def historico_temperatura():
    return render_template('temperatura.html')

@client_route.route('/umidade')
def historico_umidade():
    return render_template('umidadedoar.html')

@client_route.route('/qualidadear')
def historico_qualidadear():
    return render_template('qualidadedoar.html')

@client_route.route('/pressao')
def historico_pressao():
    return render_template('pressaoatmosferica.html')

@client_route.route('/pluviosidade')
def historico_pluviosidade():
    return render_template('pluviosidade.html')

@client_route.route("/dados")
def receber_dados():
    pass

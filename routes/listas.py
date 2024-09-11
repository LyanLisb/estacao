from flask import Blueprint, render_template, request


dados_route = Blueprint('dados',__name__)

@dados_route.route('/')
def tabela_geral ():
    return 
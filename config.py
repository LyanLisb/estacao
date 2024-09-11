from routes.home import home_route
from routes.cliente import client_route
from routes.listas import dados_route
from database.database import db
from database.models.dados import Dados

def config_all (app):
    config_routes(app)
    config_database()
    

def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(client_route,url_prefix='/historico')
    app.register_blueprint(dados_route,url_prefix='/dados')

def config_database():
    db.connect()
    db.create_tables([Dados])
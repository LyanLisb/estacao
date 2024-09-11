from peewee import Model, CharField, DateTimeField, IntegerField
from database.database import db
import datetime

class Dados(Model):
    temperatura = IntegerField()
    umidade = IntegerField()
    pressao = IntegerField()
    qualidadedoar = IntegerField()
    pluviosidade = CharField()
    date_create = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
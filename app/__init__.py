"""iniciando a aplicacao..."""

from app.config import Config
from flask import Blueprint, Flask
# from flask_sqlalchemy import SQLAlchemy

# iniciando a instancia da aplicacao
app = Flask(__name__)
blueprint = Blueprint("angosafe", __name__)

# aplicando as configuracoes ao projecto
app.config.from_object(Config)

# iniciando a instancia da base dados
# db = SQLAlchemy(app)

from app.routes import *

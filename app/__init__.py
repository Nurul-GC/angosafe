"""iniciando a aplicacao..."""

# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

from app.config import Config
from flask import Blueprint, Flask, render_template, make_response, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy

# iniciando a instancia da aplicacao
app = Flask(__name__)

# aplicando as configuracoes ao projecto
app.config.from_object(Config)

# iniciando a instancia da base dados
db = SQLAlchemy(app)

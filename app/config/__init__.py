# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

import os
from secrets import token_hex
from gcrypter import decrypt

# definindo a localizacao da base-dados
basedados_dir = os.path.abspath(os.path.dirname(__file__) + '/database')


class Config(object):
    """classe objecto com as configuracoes da app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or decrypt((3569661159, 3886674852)) or token_hex(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedados_dir, 'angosafe.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    RELOAD = False

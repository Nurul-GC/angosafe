# ************************************************
#  (c) 2019-2021 Nurul-GC                        *
# ************************************************

import os
from gcrypter import decrypt
basedir = os.path.abspath(os.path.dirname(__file__)+'/database')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or decrypt((3569661159, 3886674852))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

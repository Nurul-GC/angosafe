"""
script principal do projecto
para executa-lo basta navegar ate a localização atual do script
e digitar no terminal:
*** linux ***
    ~$: python3 ./index.py
*** windows ***
    C:/localizacao/do/script/> py index.py
"""

from app import app

if __name__ == '__main__':
    app.run()

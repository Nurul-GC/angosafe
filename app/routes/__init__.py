"""defining our routes"""

from app import app
from flask import render_template, request, jsonify, redirect, url_for
from gcrypter import encrypt, decrypt


@app.route("/", methods=['GET'])
def index():
    """pagina inicial"""
    return render_template("index.html")


@app.route("/encryption/", methods=['GET', 'POST'])
def encryption():
    """pagina encriptacao"""
    if request.query_string:
        text = request.query_string.decode().split('=')[1]
        return jsonify(encrypted=encrypt(text=text))
    elif request.method == 'POST':
        text = request.form.to_dict()['text']
        return jsonify(encrypted=encrypt(text=text))
    return render_template("encrypt.html")


@app.route("/decryption/", methods=['GET', 'POST'])
def decryption():
    """pagina desencriptacao"""
    if request.query_string:
        if '&' in request.query_string.decode():
            values = request.query_string.decode().split('&')
            value1 = int(values[0].split('=')[1])
            value2 = int(values[1].split('=')[1])
            return jsonify(decrypted=decrypt(text_enc=(value1, value2)))
        else:
            values = request.query_string.decode().split('=')[1].split(',')
            value1 = int(values[0][1:])
            value2 = int(values[1][:-1])
            return jsonify(decrypted=decrypt(text_enc=(value1, value2)))
    elif request.method == 'POST':
        values = request.form.to_dict()
        if values['value1']!='' and values['value2']!='':
            value1 = int(values['value1'])
            value2 = int(values['value2'])
            return jsonify(decrypted=decrypt(text_enc=(value1, value2))) 
        else:
            both_values = values['values'].split(',')
            value1 = both_values[0]
            value2 = both_values[1]
            if '('in value1 and ')' in value2:
                value1 = int(value1[1:])
                value2 = int(value2[:-1])
            else:
                value1 = int(value1)
                value2 = int(value2)
            return jsonify(decrypted=decrypt(text_enc=(value1, value2))) 
    return render_template("decrypt.html")


@app.route("/about/", methods=['GET'])
def about():
    """pagina de infos sobre o programa"""
    return render_template("sobre.html")

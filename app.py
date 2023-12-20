from flask import Flask, render_template,jsonify,request,redirect, url_for
from db import conectar_bd

app = Flask(__name__)

@app.after_request
def add_header(response):
  response.cache_control.no_cache = True
  return response

# Rota com a lista do Banco de Dados
@app.route('/database')
def banco_de_dados():
  conn = conectar_bd()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM usuarios")
  resultados = cursor.fetchall()
  conn.close()
  
  return render_template('banco_de_dados.html', resultado=resultados)

# Formulario
@app.route("/formulario")
def formulario():
  return render_template("formulario.html")

# Receber Formulario
@app.route("/formulario/receber", methods=['POST'])
def receber_dados():
   dados = request.get_json()
   nome = dados['nome']
   idade = dados['idade']
   
   conn = conectar_bd()
   cursor = conn.cursor()
   cursor.execute("INSERT INTO usuarios(nome, idade) VALUES (%s, %s);", (nome, idade))
   conn.commit()
   conn.close()
   
   return jsonify({'message': 'deu certo!'})

# Botao
@app.route('/botao',methods=['POST'])
def meu_botao():
  
  message= "deu certo!"
  
  return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
import mysql.connector

def conectar_bd():
  config = {
    "user":"root",
    "password":"root",
    "host":"192.168.18.141",
    "database":"Informacoes",
    "raise_on_warnings": True
  }
  return mysql.connector.connect(**config)
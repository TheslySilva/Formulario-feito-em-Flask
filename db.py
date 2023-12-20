import mysql.connector

def conectar_bd():
  config = {
    "user":"xxxx",
    "password":"xxxx",
    "host":"xxxxx",
    "database":"xxxx",
    "raise_on_warnings": True
  }
  return mysql.connector.connect(**config)
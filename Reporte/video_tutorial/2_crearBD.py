import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    )
    
    micursor=conexion.cursor()
    
    sql="create database bd_tienda"
    micursor.execute(sql)
    
except Exception as e:
    print(f"ocurrio un error por favor vuelva a intentarlo")
else:
   print(f"se creo la base de datos exitosamente")
   micursor.execute("show database")
   for x in micursor:
       print(x)

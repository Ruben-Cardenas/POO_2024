import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_tienda'
    )
except Exception as e:
    print(f"ocurrio un error por favor vuelva a intentarlo")
else:
    if conexion.is_connected():
        print(f"se creo la conexion exitosamente")
    else:
        print(f"ocurrio un problema verifiquelo")

import mysql.connector
 
#conexion con la BD de mysql
try: 
    conexion=mysql.connector.connect(
     host='localhost',
     user='root',
     password='',
     database='bd_python'
    )
except Exception as e:
 #  print(f"Error: {e}")
 #  print (f"Tipo de error {type(e).__name__}")
 print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
# else: 
#     #verificar si la conexion es correcta 
#   if conexion.is_connected():
#      print(f"se creo la conexion exitosamete")
#   else:
#      print(f"No fue posible conectar con la BD.... VERIFIQUE")



 





























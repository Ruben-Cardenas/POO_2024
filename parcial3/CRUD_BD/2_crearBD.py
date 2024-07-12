import mysql.connector
 
#conexion con la BD de mysql
try: 
    conexion=mysql.connector.connect(
     host='localhost',
     user='root',
     password='',
    )
 # crear un objeto de tipo cursot para ejecutar SQL
    micursor=conexion.cursor()
    
    sql="create database bd_python"
    
    micursor.execute(sql)
 
 
 
except Exception as e:
 print(f"Error: {e}")
 print (f"Tipo de error {type(e).__name__}")
 print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
else: 
    #verificar si la conexion es correcta 
  print (f"Se creo la BD exitosamente")
  micursor.execute("show database")
  for x in micursor:
      print(x)
 


































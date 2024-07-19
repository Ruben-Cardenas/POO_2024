from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="create table empleado (id int primary key auto_increment, nombre varchar(60),direccion varchar(120),telefono varchar(10))"
    micursor.execute(sql)
except:
    print(f"Ocurrio un error vuelva a intentarlo mas tarde")
else:
    print(f"se creo la tabla exitosamente")


  



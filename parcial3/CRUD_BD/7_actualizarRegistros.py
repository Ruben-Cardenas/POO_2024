from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="UPDATE cliente SET direccion='col. del UTD' where id=1"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
else:
    print("Registro insertado con Exito")
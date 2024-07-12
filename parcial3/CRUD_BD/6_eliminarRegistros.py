from conexionBD import *
from mysql.connector import Error

try:
    micursor=conexion.cursor()
    sql="DELETE FROM cliente WHERE direccion= 'col. del valle'"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()
except Error as e:
    print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
    print(e)
else:
    print("Registro insertado con Exito")
from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="INSERT INTO cliente (id, nombre, direccion, tel) VALUES (NULL, 'Juan Polainas', 'col. del valle', '6181223344')"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelva a intentarlo mas tarde")
else:
    print("Registro insertado con Exito")
    
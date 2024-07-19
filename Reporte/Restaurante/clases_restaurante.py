
class Platillo:
    def __init__(self, nombre, precio, ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Ingredientes: {self.ingredientes}")

    def calcular_costo(self):
        costo = self.precio
        return costo


class Desayuno(Platillo):
    def __init__(self, nombre, precio, ingredientes, fruta, tipo_desayuno):
        super().__init__(nombre, precio, ingredientes)
        self.fruta = fruta
        self.tipo_desayuno = tipo_desayuno

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fruta: {self.fruta}")
        print(f"Tipo de desayuno: {self.tipo_desayuno}")

    def calcular_costo(self):
        costo = super().calcular_costo()
       
        return costo

class Comida(Platillo):
    def __init__(self, nombre, precio, ingredientes, tipo_comida, incluye_salsas, guarniciones):
        super().__init__(nombre, precio, ingredientes)
        self.tipo_comida = tipo_comida
        self.incluye_salsas = incluye_salsas
        self.guarniciones = guarniciones

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de comida: {self.tipo_comida}")
        print(f"Incluye salsas: {self.incluye_salsas}")
        print(f"Guarniciones: {self.guarniciones}")

    def preparar_bebida(self):
        pass

    def calcular_total(self):
        total = self.precio
       
        return total


class Cena(Platillo):
    def __init__(self, nombre, precio, ingredientes, tipo_cena, bebida_alcoholica, acompañamiento):
        super().__init__(nombre, precio, ingredientes)
        self.tipo_cena = tipo_cena
        self.bebida_alcoholica = bebida_alcoholica
        self.acompañamiento = acompañamiento

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de cena: {self.tipo_cena}")
        print(f"Bebida alcohólica: {self.bebida_alcoholica}")
        print(f"Acompañamiento: {self.acompañamiento}")

    def preparar_bebida(self):
        if self.bebida_alcoholica:
            print("Preparando bebida alcohólica...")
        else:
            print("Preparando bebida no alcohólica...")

    def calcular_total(self):
        total = self.precio
       
        return total

class Bebida:
    def __init__(self, nombre, tipo_bebida, bebida_alcoholica, acompañamiento):
        self.nombre = nombre
        self.tipo_bebida = tipo_bebida
        self.bebida_alcoholica = bebida_alcoholica
        self.acompañamiento = acompañamiento

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo de bebida: {self.tipo_bebida}")
        print(f"Bebida alcohólica: {self.bebida_alcoholica}")
        print(f"Acompañamiento: {self.acompañamiento}")

    def preparar_bebida(self):
        if self.bebida_alcoholica:
            print("Preparando bebida alcohólica...")
        else:
            print("Preparando bebida no alcohólica...")



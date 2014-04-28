class Objeto(object):
    color = "Azul"
    __numero = 5
    def __init__(self, color, numero):
        self.color = color
        self.__numero = numero
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def getNumero(self):
        return self.__numero
    def setNumero(self,num):
        self.__numero = num

class Objeto2(Objeto):
    def __init__(self, numero):
        super(Objeto2, self).__init__("Violeta", numero/2)
        self.__numero = numero
    def getNumero2(self):
        return self.__numero

print("Instancia del objeto y adquisicion de un atributo  por dos metodos")
a = Objeto("Amarillo", 7)
print(a.getColor())
print(a.color)

input("\n")

print("Cambio de atributo por dos metodos distintos")
a.setColor("Verde")
print(a.color)

a.color = "Rosa Viril"
print(a.color)

input("\n")

print("Intento de acceder a atributo \"Privada\" directamente, y acceso a traves de metodo")
try:
    print(a.__numero)
except:
    print("No se puede acceder a __numero")
print(a.getNumero())

input("\n")

print("Un pequenho truco para acceder atributos y metodos \"privados\"")
print(dir(a))
print(a._Objeto__numero)

input("\n")
print("Porque existen entonces?")
b = Objeto2(12)
print(b.getNumero2())
print(b.getNumero())
print(b.__dict__)

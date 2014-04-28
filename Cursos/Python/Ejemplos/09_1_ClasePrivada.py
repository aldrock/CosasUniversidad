import re
import inspect

class Clase:
    def __init__(self):
        pass

    def privada(self, numero):
        try:
            llamada = inspect.stack()[1][4][0].strip()
            print(llamada)
            match = re.match('[a-zA-Z ]*self\.', llamada)
            if not match:
                return 'Esto es privado, largo!'
        except:
            return "Esto es privado, largo!"

        return numero**2

    def publica(self, numero):
        return self.privada(numero)


a = Clase()
print(a.privada(3))
print(a.publica(3))

def hola(self, tu):
	print("Hola,", tu)

MiLista = type('MiLista', (list,), dict(x=42, hola=hola))
#miLista ahora es una clase de tipo 
#MiLista, subclase de lista


ml = MiLista()
ml.append("Hola!")
print(ml)
print(ml.x)
print(ml.hola("Yo!"))








def except_generator(name_excp):
    """That's an except generator function"""
    return type(name_excp, (Exception,),
        {'__init__':lambda self, msg: Exception.__init__(self, msg)})


a = except_generator('YagoxError')
raise a("Que tal")
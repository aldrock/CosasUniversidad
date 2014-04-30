def ej1():
	def ej1_2():
		print("Desde 1.2")
	print("Desde 1.1")
	ej1_2()



def ej2():
	def ej2_2():
		print("Desde 2.2")
	print("Desde 2.1")
	return ej2_2




def ej3(x):
	def ej3_2():
		print(x)
	return ej3_2






def ej4(func):
	def dentro():
		print("Antes")
		func()
		print("Despues")
	return dentro






def ej5(func):
	def dentro(*args, **kargs):
		print("Estamos dentro, args=%s, kargs=%s"%(args, kargs))
		func(*args, **kargs)
	return dentro


@ej5
def ej6(*a):
	print(a)


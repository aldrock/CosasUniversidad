def func1(arg):
    print arg

def func2(fijo, *variables):
    print "Fijo:", fijo
    print "Variables:"
    for i in variables:
        print "\t",i

def func3(fijo,*args, **kargs):
    print "Fijo:", fijo
    print "Variables:"
    for i in args:
        print "\t%s" % i
    print "Kargs:"
    for i in kargs:
        print "\tClave: %s, Valor: %s" % (i, kargs[i])

def func4(fijo1, fijo2, fijo3):
    print fijo1
    print fijo2
    print fijo3


def func5(ret="", fijo="Fijo desde retorno"):
    print "Dentro de funcion con retorno1"
    return globals()[ret](fijo)

def func6(ret="", fijo="Desde retorno"):
    print "Dentro de funcion con retorno2"
    if ret in globals():
        if callable(globals()[ret]):
            return globals()[ret](fijo)
        else:
            print ret, "no es una funcion"
    else:
        print ret, "no existe"

def rec(num):
    if num<=1:
        return 1
    else:
        return num*rec(num-1)

print "Solo con un arg fijo"
func1("Test fijo")
raw_input("\n")

print "Un arg fijo, y dos variables string"
func2("VarFija", "PrimeraVar", "SegundaVar")
raw_input("\n")

print "Un arg fijo, 6 variables enteros"
func2("VarFija",1,2,3,4,5,6)
raw_input("\n")

print "Un fijo, 4 variables y 2 key args"
func3("Fija", 1,2,3,4, clave1="valor1", clave2="valor2")
raw_input("\n")

print "Llamada con un array cama parametro a los variables"
datos_var = [1500,10]
func2("Fijo", datos_var)
raw_input("\n")

print "Llamada con el mismo array pero desenpaquetando a los args variables"
func2("Fijo", *datos_var)
raw_input("\n")

print "Llamando desenpaquetando un diccionario, donde la clave es el nombre de la variable"
dicc={"fijo1": 10, "fijo2":100, "fijo3":1000}
func4(**dicc)
raw_input("\n")

print "Llamando con una fija, desenpaquetando un array para los variables y un diccionario para los kargs"
func3("Fijo", *datos_var, **dicc)
raw_input("\n")

print "Llamando de retorno"
func5("func1")
raw_input("\n")

print "Llamando de retorno con valor fijo incluido"
func5("func1","Fijo desde fuera")
raw_input("\n")

print "Llamando a una funcion que comprueba el retorno con una que no existe"
func6("funcionNoExistente")
raw_input("\n")

print "Llamando a una funcion que comprueba el retorno con una variable"
func6("dicc")
raw_input("\n")

print "Llamando a una funcion que comprueba el retorno bien"
func6("func1", "Fijo desde fuera")
raw_input("\n")

print "Usando una recursiva (factorial)"
print rec(5)
raw_input("\n")

print "Mucho recursividad no le gusta a Python!"
print rec(99999999)

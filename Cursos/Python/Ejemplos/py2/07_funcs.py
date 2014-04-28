def func1():
    print "Funcion1"

def func2():
    return "Funcion2"

def func3(arg):
    print arg

def func4(arg):
    return arg

def func5(arg1=10, arg2=100, arg3=1000):
    print arg1+arg2+arg3

def func6(arg):
    if isinstance(arg,int) or isinstance(arg,float):
        print arg, "es un numero"
    else:
        print arg, "no es un numero biatch!"


func1()
raw_input("\n")

func2()
print func2()
raw_input("\n")

var_func2 = func2()
print var_func2
raw_input("\n")

func3("Holaaa")
raw_input("\n")

func4("HolaSinPrint")
print func4("HolaConPrint")
var_func4 = func4("Hola desde variable")
print var_func4
raw_input("\n")

func5(1,2,3)
func5(0,0)
func5(arg2=0, arg3=0)
func5(arg3=9999)
raw_input("\n")

func6(10)
func6(2.2)
func6("Teeest")



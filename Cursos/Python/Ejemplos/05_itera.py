print("While desde 100 hasta que deje de ser menor que 1000)")
var = 100
while(var<1000):
    print(var)
    var+=100
print("Yay!")
input("\n")

print("Bucle infinito con break")
var = 100
while(True):
    if var>=1000:
        print("Yay!")
        break
    print(var)
    var += 100
input("\n")

print("for de lista")
mi_lista = [0,1, 2, 3]
for i in mi_lista:
    print(i)
input("\n")

print("for de tupla")
mi_tupla = (0,1,2,3)
for i in mi_tupla:
    print(i)
input("\n")

print("for de lista y tupla, pero con indice y no con valor")
for i in range(len(mi_lista)):
    print(mi_lista[i])
print()
for i in range(len(mi_tupla)):
    print(mi_tupla[i])
input("\n")

print("for con diccionario usando .keys()")
dicc = {"clave1" : 0,
        "clave2" : 1,
        "clave3" : 2,
        "clave4" : 3}

for i in dicc.keys():
    print("Clave: ", i)
    print("Valor: ", dicc[i])
    print()
input()

print("for con diccionarios sin .keys()")
for i in dicc:
    print("Clave: ", i)
    print("Valor: ", dicc[i])
    print()
input()

print("for de un diccionario con las claves ordenadas usando sorted(.keys())")
for i in sorted(dicc.keys()):
    print("Clave: %s\nValor: %s\n" % (i, dicc[i]))
input()

print("for de un diccionario con las claves ordenadas usando sorted sin .keys()")
for i in sorted(dicc):
    print("Clave",i,"\nValor:",dicc[i],"\n")

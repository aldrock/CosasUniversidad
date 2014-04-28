lista1 = [2, "Holaaa", 3.2, [1, "Esto es una lista en otra lista"], 0x69]

print("Lista completa:",lista1)
print("Elemento 0:", lista1[0])
print("Ultimo elemento [-1]: ", lista1[-1])
print("Elemento 3 (lista): ", lista1[3])
print("Elemento 1 de la lista en el elemento 3: ", lista1[3][1])
print()
lista1[0] = "much doge!"
print("Elemento 0 de la lista modificado (lista1[0] = ...)", lista1)

input("\nContinue...")
print()

lista2 = ["Parte de la lista 2", 99999]

listasuma = lista1 + lista2
print("Lista suma: ", listasuma)

lista2_mult = lista2 * 3
print("Lista 2 por 3: ", lista2_mult)

input("\nContinue...")
print()

print("Lista entera con slides [:] : ", lista1[:])
print("Lista slide [1:] :",  lista1[1:])

print("Lista slide [2:3] :", lista1[2:3])

input("\nContinue...")
print()
tupla1 = (1,2,"Hola",["List inside"])

print("Elemento 0: ", tupla1[0])
print("Ultimo elemento (-1): ", tupla1[-1])
print("Slide [1,4]: ", tupla1[1:4])

tupla2 = (1,2,3)
tupla_suma = tupla1 + tupla2
print("Sumar tuplas si se puede (tupla1 + tupla2) ", (tupla_suma))

input("\nLet's go!...")
print()
try:
    print("Intentamos modificar un elemento de la tupla1 (tupla1[0] = 4)")
    tupla1[0] = 4
except Exception as e:
    print("ERROR! No se puede modificar un elemento de la tupla")

input("\nPeeeeeero si se puede modificar una lista que este dentro: ")
print()
print("Tupla1 antes de modificar lista", tupla1)
tupla1[-1].append("Wiiii!")
print("Despues de modificarla: ", tupla1)

input("\nMetodos interesantes de las listas.")
print()
l = []
print("Lista inicial (vacia): ", l)
l.append(1)
print("Anhadimos un elemento al final: lista.append(elem) :", l)
l.append(2)
print("Anhadimos otro igual :", l)
l0 = l.pop()
print("Sacamos el ultimo elemento: elem = lista.pop() :", l, "Elem:",l0)
l = [1,2,3,4,5]
l1 = l.pop(3)
print("Se puede hacer \"pop\" de un elemento concreto: lista=[1,2,3,4,5], elem=lista.pop(3) : ", l1)
print("Lista despues del pop intermedio: ", l)

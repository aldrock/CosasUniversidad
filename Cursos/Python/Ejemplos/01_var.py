#String
a = "Hola!"
input("\nSe va a imprimir a (a=\"Hola!\") y su tipo.. ")
print(a)
print((type(a)))

#Numero
a = 4
eval(input("\nSe va a imprimir a (a=4) y su tipo.. "))
print(a)
print((type(a)))

#Division exacta
b = a / 2
eval(input("\nAhora se va a imprimir a/2... Que saldra?"))
print(b)
print((type(b)))


#Division NO exacta EN PYTHON 2!!!
c = a/3
eval(input("\nAhora a/3..."))
print(c)
print((type(c)))

d = a/3.0
d2 = float(a)/3
eval(input("\nNow... a/3 BIEN..."))
print((d,type(d)))
print((d2,type(d2)))


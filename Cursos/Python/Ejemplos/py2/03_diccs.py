dicc = {"clave1" : "valor1",
        "clave2" : "valor2",
        "clave3" : "valor3"
        }

print "Diccionario :", dicc

dicc["clave4"] = "valor4"

print "Anhadir clave (dicc[\"clave4\"] = \"valor4\") : \n", dicc

elem = dicc["clave1"]
print "Conseguimos el elemento (dicc[\"clave1\"]) : \n", elem

del dicc["clave2"]
print "Eliminamos un par (del dicc[\"clave2\"]) : \n", dicc

print "Saber las claves de un diccionario (dicc.keys() ): \n", dicc.keys()

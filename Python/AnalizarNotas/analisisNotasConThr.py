import sys
import os
from threading import *


nLock = Lock()

total = 0
aprobados8 = 0
aprobados6= 0
aprobados5 = 0
suspensosMas4 = 0
suspensosMenor4=0
NP = 0

def analizarNota(*nota):
    notaProv = ""
    for i in nota:
        notaProv += i
    nota = notaProv
    
    global total,aprobados8 , aprobados6 ,aprobados5 , suspensosMas4, suspensosMenor4, NP

    if nota=="np":
        with nLock:
            total +=1
            NP+=1
        return
       
    nota = float(nota)
    if nota<=10.0 and nota>=8.0:
        with nLock:
            total +=1
            aprobados8+=1
        return
    elif nota>=6.0:
        with nLock:
            total +=1
            aprobados6+=1
        return
    elif nota>=5.0:
        with nLock:
            total +=1
            aprobados5+=1
        return
    elif nota>=4.0:
        with nLock:
            total +=1
            suspensosMas4+=1
        return
    else:
        with nLock:
            total +=1
            suspensosMenor4+=1
        return



def analisisNotas(path):

    thr = []
    #Se lee el archivo
    with open(path, "r") as f:
        for line in f:
            nota=line.split(";")[-1].strip("\r").strip("\n") #Se coge la nota
            t = Thread(target=analizarNota, args=(nota)) #Se va a crear un thread, y cada uno analizara la nota
            t.start()
            thr.append(t)
    #Se espera a los procesos
    for i in thr:
        i.join()

    return


def main():
    if len(sys.argv) < 2:
        sys.exit('Uso: %s <nombreArchivoNotas>' % sys.argv[0])

    if not os.path.exists(sys.argv[1]):
        sys.exit('ERROR: Archivo de notas %s no encontrado!' % sys.argv[1])  

    path = sys.argv[1]  

    analisisNotas(path)

    aprobadosTotal = aprobados8+aprobados6+aprobados5
    suspensosTotal = suspensosMas4 + suspensosMenor4

    porcConNP = (aprobadosTotal / float(total)) * 100
    porcSinNP = (aprobadosTotal / (float(total) - NP)) * 100

    print """
|-----------------------------------------------|    
    Total: %s                                  
|-----------------------------------------------|
    Aprobados total: %s                        
        Aprobados entre 8 y 10: %s             
        Aprobados entre 6 y 8: %s              
        Aprobados entre 5 y 6: %s              
|-----------------------------------------------|
    Suspensos total: %s                        
        Suspensos entre 4 y 5: %s              
        Suspensos con menos de 4: %s           
|-----------------------------------------------|
    NP: %s                                     
                                               
    Porcentaje aprobados con NP: %.2f%% (%s/%s)       
    Porcentaje aprobados sin NP: %.2f%% (%s/%s)       
|-----------------------------------------------|
    """ % (total, aprobadosTotal, aprobados8,aprobados6, aprobados5, suspensosTotal, 
        suspensosMas4, suspensosMenor4, NP, porcConNP,aprobadosTotal,total, porcSinNP, aprobadosTotal, total-NP)

if __name__ == "__main__":
    main()


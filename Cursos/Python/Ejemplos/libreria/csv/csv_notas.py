import csv
import sys

def read_csv(f_obj):
    reader = csv.reader(f_obj, delimiter=";")
    for fila in reader:
        print(" - ".join(fila))
        #Hacer lo que se quiera, es una lista con los campos


def read_csv_dict(f_obj):
    reader = csv.DictReader(f_obj, delimiter=";")
    for linea in reader:
        print("{0} - {1}".format(linea["nombre"], linea["matricula"]))


def read_meta(function):
    with open("notas", "rU") as f:
        function(f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("command: {} <norm/dict>".format(sys.argv[0]))
        exit(1)
    command = sys.argv[1]
    if command == "norm":
        read_meta(read_csv)
    elif command == "dict":
        read_meta(read_csv_dict)
    else:
        print("command: {} <norm/dict>".format(sys.argv[0]))
        exit(1)

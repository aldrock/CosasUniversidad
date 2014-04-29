import csv
import sys

def csv_writer(data, path):
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerows(data)
        #for line in data:
        #    writer.writerow(line)



def csv_dict_writer(data, fields, path):
    with open(path, "w") as f:
        writer = csv.DictWriter(f, delimiter=";", fieldnames=fields)
        writer.writeheader()
        #writer.writerows(data)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("command: {} <norm/dict>".format(sys.argv[0]))
        exit(1)

    data = ["nombre;matricula;nota1;nota2;nota3".split(";"),
                "AGUADO PEÑA, JUAN;100200;5.0;1.5;6.5".split(";"),
                "AGUDO BALLESTEROS, MIGUEL;110022;0;2.0;2.0".split(";"),
                "ALAOUI SOSSAI, MAHDI;050275;8.0;0.0;8.0".split(";"),
                "ALEJANDRE SANCHEZ, CARLOS;100202;np;np;np".split(";")
                ]
	"""
	data (lista de listas):
	[
		["nombre", "matricula", "nota1", "nota2", "nota3"],
		["AGUADO PEÑA, JUAN", "100200", 5.0, 1.5, 6.5],
	...
	]
	"""
    command = sys.argv[1]
    if command == "norm":
        csv_writer(data, "csv_writed.csv")
    elif command == "dict":
        my_data = []
        fields = data[0] #cabecera (lista):  ["nombre", "matricula", "nota1", "nota2", "nota3"]
        for values in data[1:]:
            my_data.append(dict(zip(fields, values)))
        """
        zip crea un array con tuplas:
        [("nombre", "AGUADO PEÑA, JUAN"), ("matricula", "100200",  ("nota1", 5.0), ("nota2", 1.5), ("nota3", 6.5)]
        dict transforma ese array de tuplas a diccionario:
        {"nombre": "AGUADO PEÑA, JUAN", "matricula": "100200",  "nota1": 5.0,  "nota2": 1.5, "nota3": 6.5}
        Al final queda una lista de diccionarios:
        [
        	{"nombre": "AGUADO PEÑA, JUAN", "matricula": "100200",  "nota1": 5.0,  "nota2": 1.5, "nota3": 6.5}
        	{"nombre": "AGUDO BALLESTEROS, MIGUEL", "matricula": "110022",  "nota1": 0,  "nota2": 2.0, "nota3": 2.0}
        	...
        ]
        """
        csv_dict_writer(my_data, fields, "csv_writed.csv")
    else:
        print("command: {} <norm/dict>".format(sys.argv[0]))
        exit(1)


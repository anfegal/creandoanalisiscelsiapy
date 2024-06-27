import random
def generarDatos(): 
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["sabaneta","estrella","medellin","copacabana","caldas"])
        responsable=random.choice(["Ana Sofia Gallego","Juan Jose Gallego","Johana Andrea Quiroga", "Juan Esteban Gallego","Martha Lilia Alzate"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)

    return datos

print (generarDatos())

from typing import NamedTuple
from datetime import datetime
from pathlib import Path
import csv
from typing import List

Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])

def lee_carreras(ruta : str) ->list[CarreraFP]:
    carreras =[] 
    with open(ruta, "r", encoding="utf-8") as fichero: 
        lector = csv.reader(fichero, delimiter=",")
        next(lector) 
        for campos in lector:
            fecha_hora = datetime.strptime(campos[0], "%Y-%m-%d %H:%M")
            circuito = campos[1]
            pais = campos[2]
            seco = campos[3] == "si"
            tiempo = float(campos[4])
            podio = [Piloto(nombre=campos[5], escuderia=campos[6]),
                     Piloto(nombre=campos[7], escuderia=campos[8]),
                     Piloto(nombre=campos[9], escuderia=campos[10])]
            carrera=CarreraFP(fecha_hora=fecha_hora, circuito=circuito, pais=pais, seco=seco, tiempo=tiempo, podio=podio)    
            carreras.append(carrera)
    return carreras
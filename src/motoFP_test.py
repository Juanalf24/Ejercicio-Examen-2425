from motoFP import lee_carreras
from typing import NamedTuple
from datetime import datetime
from pathlib import Path
import csv
from typing import List

if __name__ == "__main__":
    ruta=Path("data/mundial_motofp.csv")
    carreras = lee_carreras(ruta)
    print(carreras[:2])
    print(carreras[:-2])
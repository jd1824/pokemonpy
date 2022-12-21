from ensurepip import version
import time
import numpy as np
import sys

def imprimir_con_retraso(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud="================"):
        self.nombre = nombre
        self.tipos = tipos
        self. movimientos = movimientos
        self.ataque = EVs["ataque"]
        self.defensa = EVs["defensa"]
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20

def impresa(self, pokemon2):
    print("-----BATALLA POKéMON-----")
    print(f"\n{self.nombre}")
    print("tipo/", self.tipos)
    print("ataque/", self.ataque)
    print("defensa/", self.defensa)
    print("Nv./", 3*(1+np.mean([self.ataque,self.defensa])))
    print("\nVS")
    print(f"\n{pokemon2.nombre}")
    print("tipo/", pokemon2.tipos)
    print("ataque/", pokemon2.ataque)
    print("defensa/", pokemon2.defensa)
    print("Nv./", 3*(1+np.mean([pokemon2.ataque,pokemon2.defensa])))
    time.sleep(2)

def ventaja(self,pokemon2):
    version = ["fuego", "agua", "planta"]
    for i,k in enumerate(version):
        
        if self.tipos == k:
            if pokemon2.tipos == k:
                cadena_1_ataque = "\nNo es muy efectivo..."
                cadena_2_ataque = "\nNo es muy efectivo..."

            if pokemon2.tipos == version[(i+1)%3]:
                pokemon2.ataque *= 2
                pokemon2.defensa *= 2
                self.ataque /= 2
                self.defensa /= 2
                cadena_1_ataque = "\nNo es muy efectivo..."
                cadena_2_ataque = "\n¡es muy eficaz!"

            if pokemon2.tipos == version[(i+2)%3]:
                self.ataque *= 2
                self.defensa *= 2
                pokemon2.ataque /= 2
                pokemon2.defensa /= 2
                cadena_1_ataque = "\n!es muy eficaz¡"
                cadena_2_ataque = "\nNo es muy efectivo..."

            return cadena_1_ataque, cadena_2_ataque

def turno(self, pokemon2, cadena_1_ataque, cadena_2_ataque):
    while  (self.barras > 0) and (pokemon2.barras > 0):
        print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
        print(f"\n{pokemon2.nombre}\t\tPS\t{pokemon2.puntos_de_salud}\n")

        #POKEMON 1
        print(f"!adelante {self.nombre}¡")
        for i, x in enumerate(self.movimientos):
            print(f"{i+1}.", x)
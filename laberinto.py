import os
import random
from typing import List, Tuple
from readchar import readkey, key

class Juego:
    # Constructor de la clase Juego.
    def __init__(self, mapa: List[List[str]], inicio: Tuple[int, int], fin: Tuple[int, int]):
        # Inicializa el mapa del juego y las posiciones de inicio y fin.
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    # Convierte un string que representa un laberinto en una matriz.
    def convertir_mapa_a_matriz(self, laberinto: str) -> List[List[str]]:
        # Divide el string por líneas y convierte cada línea en una lista.
        return [list(fila) for fila in laberinto.split("\n")]

    # Muestra el mapa actual en la consola.
    def mostrar_mapa(self):
        # Limpia la pantalla antes de mostrar el mapa.
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in self.mapa:
            print(''.join(fila))

    # Contiene el bucle principal del juego para el movimiento del jugador.
    def main_loop(self):
        # Inicializa la posición del jugador.
        px, py = self.inicio
        self.mapa[px][py] = 'P'

        # Bucle que se ejecuta hasta que el jugador alcanza la posición final.
        while (px, py) != self.fin:
           # Agregar para depuración
            self.mostrar_mapa()
            movimiento = readkey()

            # Determina la nueva posición basada en la entrada del jugador.
            nueva_px, nueva_py = px, py
            if movimiento == key.UP:
                nueva_px -= 1
            elif movimiento == key.DOWN:
                nueva_px += 1
            elif movimiento == key.LEFT:
                nueva_py -= 1
            elif movimiento == key.RIGHT:
                nueva_py += 1

            # Actualiza la posición del jugador si el movimiento es válido.
            if 0 <= nueva_px < len(self.mapa) and 0 <= nueva_py < len(self.mapa[0]) and self.mapa[nueva_px][nueva_py] != '#':
                self.mapa[px][py] = '.'
                px, py = nueva_px, nueva_py
                self.mapa[px][py] = 'P'
                print("Llegaste al final del laberinto")

class JuegoArchivo(Juego):
    # Constructor de la clase JuegoArchivo.
    def __init__(self, path_a_mapas: str):
        # Elige un mapa de laberinto al azar de un directorio y lee los datos.
        archivo_mapa = self.elegir_mapa_aleatorio(path_a_mapas)
        mapa, inicio, fin = self.leer_datos_mapa(archivo_mapa)
        super().__init__(mapa, inicio, fin)

    # Elige un archivo de mapa al azar de un directorio.
    def elegir_mapa_aleatorio(self, path: str) -> str:
        archivos = os.listdir(path)
        nombre_archivo = random.choice(archivos)
        return f"{path}/{nombre_archivo}"

    # Lee los datos del mapa desde un archivo.
    def leer_datos_mapa(self, archivo_mapa: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
        with open(archivo_mapa, 'r') as file:
            lineas = file.readlines()
        
        # Extrae las coordenadas de inicio y fin del mapa.
        coords = lineas[0].strip().split()
        inicio = (int(coords[0]), int(coords[1]))
        fin = (int(coords[2]), int(coords[3]))
        laberinto = ''.join(lineas[1:]).strip()

        # Convierte el laberinto en una matriz y lo retorna junto con las coordenadas.
        mapa = self.convertir_mapa_a_matriz(laberinto)
        return mapa, inicio, fin

def main():
    # Crea una instancia de JuegoArchivo y comienza el juego.
    juego = JuegoArchivo("./mapas")
    juego.main_loop()

if __name__ == "__main__":
    main()

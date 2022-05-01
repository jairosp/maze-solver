


class Laberinto():
    def __init__(self, dimension, muro):
        self.dimension = dimension
        self.muro = muro
        self.array = self.array()

    def array(self):
        laberinto = list() # Creamos el laberinto en forma de lista y añadimos cada fila como otra lista

        for i in range(self.dimension[0]):
            fila = list()
            
            for j in range(self.dimension[1]):

                verificador = 0 # Verifica coincidencia de (i,j) con muro
                for element in self.muro:
                        
                        if (i,j) == element:
                            verificador += 1
                        


                if verificador == 1:
                    fila.append('X')

                else:
                    fila.append(' ')
                
            laberinto.append(fila)

        
        return laberinto

    def mostrar(self):
        print(40*"=")
        print("\n\tMAPA DEL LABERINTO\n")
        for fila in self.array:
            print("\t",fila)
        print("\n",40*"=", 2*"\n")
        
    def resolver(self):
        coordenada_actual = (0,0)
        coordenada_objetivo = (self.dimension[0] - 1, self.dimension[1] - 1) #En el ejercicio se especifica que la casilla final es la (m,n) siendo el laberinto mxn. Como python empieza a contar en 0, restamos 1.

        camino_recorrido = [coordenada_actual] # Array de casillas ya recorridas

        instrucciones = []
        puntos_multi_camino = [] # Esta lista guarda los puntos de multiple camino y la longitud de la lista de direcciones en ese punto.

        def dar_instrucciones(primera_casilla, segunda_casilla):
            if primera_casilla[0] == segunda_casilla[0]:
                if primera_casilla[1] + 1 == segunda_casilla[1]:
                    return "Derecha"
                if primera_casilla[1] - 1 == segunda_casilla[1]:
                    return "Izquierda"
            elif primera_casilla[1] == primera_casilla[1]:
                if primera_casilla[0] + 1 == segunda_casilla[0]:
                    return "Abajo"
                if primera_casilla[0] - 1 == segunda_casilla[0]:
                    return "Arriba"
            else:
                raise Exception("Error, casillas no contiguas")


        while coordenada_actual != coordenada_objetivo:
            # Comprobar casillas alrededor
            alrededor = []
            

            for i in (coordenada_actual[0] - 1, coordenada_actual[0], coordenada_actual[0] + 1):
                for j in (coordenada_actual[1] - 1, coordenada_actual[1], coordenada_actual[1] + 1):

                    dentro_del_laberinto = i>=0 and j>= 0 and i<self.dimension[0] and j<self.dimension[1]
                    no_esta_en_diagonal = (coordenada_actual[0] + coordenada_actual[1]) % 2 != (i+j)%2 # Usando propiedades de matrices dos elementos están en diagonal cuando la suma de sus coordenadas es congruente modulo 2 a la otra suma de coordenadas.
                    no_es_la_misma_casilla = (i,j) != (coordenada_actual[0],coordenada_actual[1])

                    if dentro_del_laberinto and no_es_la_misma_casilla and no_esta_en_diagonal:
                        alrededor.append((i,j))

            # Contar casillas posibles alrededor

            casillas_libres = []
            for casilla in alrededor:

                casilla_libre = self.array[casilla[0]][casilla[1]] != 'X'

                if (casilla not in camino_recorrido) and casilla_libre:
                    casillas_libres.append(casilla)

            # Actuamos segun el numero de casillas libres

            # Algoritmo de resolucion con 1 camino posible, avanzar.
            if len(casillas_libres) == 1:
                instrucciones.append(dar_instrucciones(coordenada_actual,casillas_libres[0]))
                coordenada_actual = casillas_libres[0]
                camino_recorrido.append(coordenada_actual)

            # En caso de múltiples casillas, guardamos el punto de decision y avanzamos para volver en caso de error
            elif len(casillas_libres) > 1:

                puntos_multi_camino.append((coordenada_actual, len(instrucciones)))
                instrucciones.append(dar_instrucciones(coordenada_actual,casillas_libres[0]))

                coordenada_actual = casillas_libres[0]
                camino_recorrido.append(coordenada_actual)

            # En caso de no encontrar salida, volvemos al punto de decision anterior
            elif len(casillas_libres) == 0:
                try:
    
                    datos_ultimo_punto = puntos_multi_camino.pop()
                    coordenada_actual = datos_ultimo_punto[0] # Vuelve al último punto de multiple opcion
                    longitud_lista_punto_anterior = datos_ultimo_punto[1]
                    while len(instrucciones) > longitud_lista_punto_anterior:
                        instrucciones.pop()

                except:
                    raise Exception("Laberinto sin salida")

        print("Laberinto Resuelto!!")
        print(instrucciones)


if __name__ == '__main__':
    muro = ((0,1), (0,3), (0,4), (1,1), (2,1), (1,3), (3,3), (4,0), (4,1), (4,2), (4,3)) # Tupla con coordenadas de los muros
    dimension = (5,5) # Filas, columnas
    mi_laberinto = Laberinto(dimension, muro)
    mi_laberinto.mostrar()
    mi_laberinto.resolver()

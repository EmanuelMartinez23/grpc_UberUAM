import grpc
import random
import math
import string
import uber_proto_pb2
import uber_proto_pb2_grpc
from concurrent import futures

# Clase Auto
class Auto:
    # constructor de la clase 
    def __init__(self, id_auto,x, y,disponible=None, tipo_uber=None):
        self.id_auto = id_auto
        self.x = x
        self.y = y
        self.disponible = disponible
        # se cre con un de los tres tipos de Uber
        self.tipo_uber = tipo_uber if tipo_uber else random.choice([uber_proto_pb2.tipo_uber.Uber_Planet, uber_proto_pb2.tipo_uber.Uber_XL, uber_proto_pb2.tipo_uber.Uber_Black])

    #función para generar placas aleatorias(3 letras y 3 números)
    def generarPlacas(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))  # 3 letras aleatorias
        numeros = ''.join(random.choices(string.digits, k=3))  # 3 números aleatorios
        return f"{letras}-{numeros}"

# Servidor para manejar las solicitudes
# Clase que hereda de una de las clases generadas con los proto
class SolicitarViajeServicer(uber_proto_pb2_grpc.SolicitarViajeServicer):

    # Inciializamos la clase generando 10 autos usando nuestra clase anterior
    def __init__(self):
        self.autos = []
        
        for i in range(10):
            # Generamos posiciónes aleatoria para cada auto
            x = random.randint(0, 50)
            y = random.randint(0, 50)
            # Aleatoriamente asignamos la dispoibilidad (con dos opciones)
            disponible = random.choice([True, False])
            # Creamos el auto y lo añadimos a la lista
            self.autos.append(Auto(id_auto=i, x=x, y=y, disponible=disponible))

    def InfoAuto(self, request, context):
        #Coordenadas del cliente
        cliente_x = request.x
        cliente_y = request.y

        # Autos disponibles
        autos_disponibles = [auto for auto in self.autos if auto.disponible]

        if not autos_disponibles:
            context.set_details('No hay autos disponibles')
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return uber_proto_pb2.InfoResponse()

        # Función para calcular la distancia Euclidiana
        def calcular_distancia(auto):
            return math.sqrt((auto.x - cliente_x) ** 2 + (auto.y - cliente_y) ** 2)

        # encontramos el automa más cercano de los disponibles
        auto_mas_cercano = min(autos_disponibles, key=calcular_distancia)

        # Obtener tarifa según el tipo de Uber
        if auto_mas_cercano.tipo_uber == uber_proto_pb2.tipo_uber.Uber_Planet:
            tarifa = 10
        elif auto_mas_cercano.tipo_uber == uber_proto_pb2.tipo_uber.Uber_XL:
            tarifa = 15
        else:
            tarifa = 25

        # Crear la respuesta con el auto más cercano disponible
        response = uber_proto_pb2.InfoResponse(
            disponible=auto_mas_cercano.disponible,
            coordenadas=uber_proto_pb2.Posicion(x=auto_mas_cercano.x, y=auto_mas_cercano.y),
            uber=auto_mas_cercano.tipo_uber,
            tarifa=tarifa,
            placas=auto_mas_cercano.generarPlacas(),
        )
        return response

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    uber_proto_pb2_grpc.add_SolicitarViajeServicer_to_server(SolicitarViajeServicer(), server)
    server.add_insecure_port('[::]:' + port)
    print(f"Server UberUAM {port}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

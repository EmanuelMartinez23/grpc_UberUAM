import grpc
import math
import string
import random
from concurrent import futures
import uber_proto_pb2
import uber_proto_pb2_grpc

# Clase para Autos
class Auto:
    def __init__(self, id_auto, x, y, disponible):
        self.id_auto = id_auto
        self.x = x
        self.y = y
        self.disponible = disponible
        # Usamos un string para representar el tipo de Uber
        self.tipo_uber = random.choice(["Uber_Planet", "Uber_XL", "Uber_Black"])
        # Generamos placas una sola vez en el constructor
        self.placas = f"{''.join(random.choices(string.ascii_uppercase, k=3))}-{''.join(random.choices(string.digits, k=3))}"

    def obtenerPlacas(self):
        return self.placas

class SolicitarViajeServicer(uber_proto_pb2_grpc.SolicitarViajeServicer):
    def __init__(self):
        # lista de autos
        self.autos = []
        # viajes realizados
        self.viajes_realizados = 0
        # ganancia
        self.ganancia_total = 0
        # Creamos los 10 autos
        for i in range(10):
            x = random.randint(0, 50)
            y = random.randint(0, 50)
            disponible = random.choice([True, False])
            self.autos.append(Auto(id_auto=i, x=x, y=y, disponible=disponible))

    def InfoAuto(self, request, context):
        cliente_x, cliente_y = request.x, request.y
        autos_disponibles = [auto for auto in self.autos if auto.disponible]

        if not autos_disponibles:
            context.set_details('No hay autos disponibles')
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return uber_proto_pb2.InfoResponse()

        # función para calcular la distancia
        def calcular_distancia(auto):
            return math.sqrt((auto.x - cliente_x) ** 2 + (auto.y - cliente_y) ** 2)

        # Obtenemos el auto más cercano
        auto_mas_cercano = min(autos_disponibles, key=calcular_distancia)
        tarifa = {
            "Uber_Planet": 10,
            "Uber_XL": 15,
            "Uber_Black": 25,
        }[auto_mas_cercano.tipo_uber]

        # respuesta
        response = uber_proto_pb2.InfoResponse(
            disponible=True,
            coordenadas=uber_proto_pb2.Posicion(x=auto_mas_cercano.x, y=auto_mas_cercano.y),
            uber=auto_mas_cercano.tipo_uber,  # Ahora es un string
            tarifa=tarifa,
            placas=auto_mas_cercano.obtenerPlacas(),  # Usar las placas fijas
        )

        # Después de la respuesta, colocamos que no está disponible ya que está en un viaje
        auto_mas_cercano.disponible = False
        return response

    def TerminarViaje(self, request, context):
        # Buscamos el auto por las placas para terminar el viaje
        auto = next((auto for auto in self.autos if auto.placas == request.placas), None)
        
        if not auto:
            context.set_details('Auto no encontrado')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return uber_proto_pb2.TerminarViajeResponse(exito=False)

        # Actualizamos la posición del auto y marcamos como disponible después de terminar el viaje
        auto.x, auto.y = request.posicion_final.x, request.posicion_final.y
        auto.disponible = True
        
        # Registrar el viaje en las estadísticas del servidor
        self.viajes_realizados += 1
        self.ganancia_total += request.costo_viaje

        return uber_proto_pb2.TerminarViajeResponse(exito=True)

    def EstadoServicio(self, request, context):
        autos_libres = sum(auto.disponible for auto in self.autos)
        response = uber_proto_pb2.EstadoServicioResponse(
            viajes_realizados=self.viajes_realizados,
            autos_libres=autos_libres,
            ganancia_total=self.ganancia_total,
        )
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    uber_proto_pb2_grpc.add_SolicitarViajeServicer_to_server(SolicitarViajeServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Uber UAM: Servidor iniciado en el puerto 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

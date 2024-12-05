import grpc
import uber_proto_pb2
import uber_proto_pb2_grpc
import random
import time
import sys
import math

# cliente para pasajeros
def cliente_pasajero(stub):
    # Generar posiciones de origen y destino aleatorias para la request
    origen = uber_proto_pb2.Posicion(x=random.randint(0, 50), y=random.randint(0, 50))
    destino = uber_proto_pb2.Posicion(x=random.randint(0, 50), y=random.randint(0, 50))

    # Log
    print(f"Posición de origen: ({origen.x}, {origen.y})")
    print(f"Posición de destino: ({destino.x}, {destino.y})")

    try:
        # Solicitamos un auto pasando las coordenadas de incio
        response = stub.InfoAuto(origen)
        # Log 
        print(f"Auto encontrado: {response.placas}, Tipo: {uber_proto_pb2.tipo_uber.Name(response.uber)}, Tarifa: {response.tarifa}")

        # Calculamos distancia para generar la ganacia y simular viaje
        distancia = math.sqrt((origen.x - destino.x) ** 2 + (origen.y - destino.y) ** 2)
        # Log
        print(f"Distancia del viaje: {distancia:.2f}")
        # Simulación del viaje
        time.sleep(distancia * 0.1)

        # Calculamos el costo del viaje
        costo = int(response.tarifa * distancia)
        print(f"Costo del viaje: {costo}")

        # Terminamos el viaje
        terminar_request = uber_proto_pb2.TerminarViajeRequest(posicion_final=destino, placas=response.placas, costo_viaje=costo)
        terminar_response = stub.TerminarViaje(terminar_request)
        # Log
        if terminar_response.exito:
            print("Viaje terminado exitosamente.")
        else:
            print("Error al terminar el viaje: Verifique si las placas coinciden con las registradas.")

    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

# Cliente para administradores 
def cliente_administrador(stub):
    try:
        # Bucle infinito para obtener en tiempo real los cambios
        while True:
            # con el stub coinseguimos el servicio de estadoServicio y traer las estadisticas
            response = stub.EstadoServicio(uber_proto_pb2.Empty())
            #Log
            print(f"Viajes realizados: {response.viajes_realizados}, Autos libres: {response.autos_libres}, Ganancia total: {response.ganancia_total}")
            # Consultar cada 2 segundos
            time.sleep(2)
    except KeyboardInterrupt:
        print("Administrador detenido.")


# funcion principal para el cliente
def cliente():
    # Uso del cliente, parametros solo sea uno
    if len(sys.argv) < 2:
        print("Uso: python client.py <rol>\nRoles: pasajero, administrador")
        return
    # el role es el primer parametro posicional    
    rol = sys.argv[1]
    # creamos un canal de comunicación en  IP y Host dicha.
    channel = grpc.insecure_channel('localhost:50051')
    # Stub que va mantener los métodos remotos como locales
    stub = uber_proto_pb2_grpc.SolicitarViajeStub(channel)
    # dependiendo el rol lanzar la función
    if rol == "pasajero":
        cliente_pasajero(stub)
    elif rol == "administrador":
        cliente_administrador(stub)
    else:
        print("Rol no válido. Use 'pasajero' o 'administrador'.")

if __name__ == "__main__":
    cliente()

import grpc
import uber_proto_pb2
import uber_proto_pb2_grpc

def run():
    # Crear un canal de comunicación con el servidor
    channel = grpc.insecure_channel('localhost:50051')
    stub = uber_proto_pb2_grpc.SolicitarViajeStub(channel)
    
    # Crear la solicitud con las coordenadas del cliente
    request = uber_proto_pb2.Posicion(x=60, y=30)  # Ejemplo de posición cliente

    # Hacer la llamada al servidor
    response = stub.InfoAuto(request)
    
    print("Respuesta del servidor:")
    print(f"Disponible: {response.disponible}")
    print(f"Coordenadas del auto más cercano: x={response.coordenadas.x}, y={response.coordenadas.y}")
    
    # Convertir el valor entero de 'response.uber' a su nombre legible
    tipo_uber_nombre = uber_proto_pb2.tipo_uber.Name(response.uber)  # Usamos el método Name() para obtener el nombre
    
    print(f"Tipo de Uber: {tipo_uber_nombre}")  # Muestra el nombre del tipo de Uber
    print(f"Tarifa: {response.tarifa}")
    print(f"Placas: {response.placas}")

if __name__ == "__main__":
    run()

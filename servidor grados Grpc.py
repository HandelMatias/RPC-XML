from concurrent import futures
import grpc
import grados_pb2
import grados_pb2_grpc

class ConversorTemperatura(grados_pb2_grpc.TemperaturaServicer):

    def CelsiusAFahrenheit(self, request, context):
        resultado = (request.valor * 9/5) + 32
        return grados_pb2.TemperaturaResponse(resultado=resultado)

    def FahrenheitACelsius(self, request, context):
        resultado = (request.valor - 32) * 5/9
        return grados_pb2.TemperaturaResponse(resultado=resultado)

def servir():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    grados_pb2_grpc.add_TemperaturaServicer_to_server(
        ConversorTemperatura(), server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("Servidor gRPC ejecutándose en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    servir()
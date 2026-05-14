import grpc
import grados_pb2
import grados_pb2_grpc

canal = grpc.insecure_channel('localhost:50051')
stub = grados_pb2_grpc.TemperaturaStub(canal)

while True:

    print("\n=== CONVERSOR DE TEMPERATURA gRPC ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "3":
        print("Saliendo del sistema...")
        break

    if opcion in ["1", "2"]:

        valor = float(input("Ingrese la temperatura: "))

        if opcion == "1":
            respuesta = stub.CelsiusAFahrenheit(
                grados_pb2.TemperaturaRequest(valor=valor)
            )

            print(f"Resultado: {respuesta.resultado} °F")

        elif opcion == "2":
            respuesta = stub.FahrenheitACelsius(
                grados_pb2.TemperaturaRequest(valor=valor)
            )

            print(f"Resultado: {respuesta.resultado} °C")

    else:
        print("Opción inválida")
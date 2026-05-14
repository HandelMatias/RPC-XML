import grpc
import calculadora_pb2
import calculadora_pb2_grpc

#Crea el canal de comunicacion
canal = grpc.insecure_channel(
    'localhost:5000'
)

#Crea el stub que es el cliente automatico
stub = calculadora_pb2_grpc.CalculadoraStub(
    canal
)

while True:
    print("\n--- CALCULADORA RPC ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion >= "5":
        break
    
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    operacion = calculadora_pb2.Operacion(a=a, b=b)

    try:
        if opcion == "1":
            r = stub.Sumar(operacion)
        elif opcion == "2":
            r = stub.Restar(operacion)
        elif opcion == "3":
            r = stub.Multiplicar(operacion)
        elif opcion == "4":
            r = stub.Dividir(operacion)
        else:
            print("Opción inválida")
            continue

        print("Resultado:", r.r)

    except grpc.RpcError as e:
        print("Error:", e.details())



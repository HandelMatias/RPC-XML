import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    print("\n--- CONVERSOR DE TEMPERATURA XML-RPC ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion >= "3":
        break

    temp = float(input("Ingrese la temperatura: "))

    if opcion == "1":
        resultado = proxy.c_to_f(temp)
    elif opcion == "2":
        resultado = proxy.f_to_c(temp)
    else:
        print("Opción inválida")
        continue

    print("Resultado:", resultado)
import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    print("\n=== CALCULADORA XML-RPC ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo de la calculadora...")
        break

    if opcion in ["1", "2", "3", "4"]:

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = cliente.sumar(num1, num2)
            print(f"Resultado de la suma: {resultado}")

        elif opcion == "2":
            resultado = cliente.restar(num1, num2)
            print(f"Resultado de la resta: {resultado}")

        elif opcion == "3":
            resultado = cliente.multiplicar(num1, num2)
            print(f"Resultado de la multiplicación: {resultado}")

        elif opcion == "4":
            resultado = cliente.dividir(num1, num2)
            print(f"Resultado de la división: {resultado}")

    else:
        print("Opción inválida. Intente nuevamente.")
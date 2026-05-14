import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")

cliente.sumar(5,4)
print("La suma es: ", r)

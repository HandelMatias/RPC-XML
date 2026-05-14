from xmlrpc.server import SimpleXMLRPCServer

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_function(sumar, "sumar")
server.register_function(restar, "restar")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")

print("Servidor XML-RPC ejecutándose en http://localhost:8000")
server.serve_forever()
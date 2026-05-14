from xmlrpc.server import SimpleXMLRPCServer

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor XML-RPC ejecutándose...")

server.register_function(celsius_a_fahrenheit, "c_to_f")
server.register_function(fahrenheit_a_celsius, "f_to_c")

server.serve_forever()
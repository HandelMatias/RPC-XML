```markdown
# RPC-XML

Este repositorio contiene ejercicios prácticos de comunicación entre cliente y servidor usando **XML-RPC** y **gRPC** en Python.

La idea principal del proyecto es mostrar cómo dos programas pueden intercambiar información aunque estén separados, usando llamadas remotas a procedimientos. Se trabajan ejemplos sencillos como una calculadora y conversión de grados, para entender mejor la estructura de cada tecnología.

## Contenido del proyecto

- Ejercicios con **XML-RPC**
- Ejercicios con **gRPC**
- Cliente y servidor para calculadora
- Cliente y servidor para conversión de grados
- Archivos `.proto` para definir los servicios de gRPC
- Archivos generados por Protocol Buffers

## Tecnologías usadas

- Python
- XML-RPC
- gRPC
- Protocol Buffers

## Archivos principales

| Archivo | Descripción |
|---|---|
| `Servidor grados XML-RPC.py` | Servidor XML-RPC para conversión de grados |
| `Cliente grados XML-RPC.py` | Cliente XML-RPC para conversión de grados |
| `servidor grados Grpc.py` | Servidor gRPC para conversión de grados |
| `cliente grados Grpc.py` | Cliente gRPC para conversión de grados |
| `servidor calcu XML-RPC.py` | Servidor XML-RPC para calculadora |
| `cliente calcu XML-RPC.py` | Cliente XML-RPC para calculadora |
| `servidor calcu Grpc.py` | Servidor gRPC para calculadora |
| `calculadora.proto` | Definición del servicio de calculadora |
| `grados.proto` | Definición del servicio de conversión de grados |

## Cómo ejecutar

Primero instala las dependencias necesarias:

```bash
pip install grpcio grpcio-tools
```

Para ejecutar un ejemplo, primero abre una terminal y ejecuta el servidor:

```bash
python "servidor grados Grpc.py"
```

Luego abre otra terminal y ejecuta el cliente:

```bash
python "cliente grados Grpc.py"
```

El mismo proceso aplica para los demás ejercicios: primero se inicia el servidor y después el cliente correspondiente.

## Generar archivos gRPC

Si necesitas volver a generar los archivos de gRPC desde los `.proto`, puedes usar:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. grados.proto
```

## Conclusión

Este proyecto ayudó a comprender cómo funcionan las llamadas remotas usando XML-RPC y gRPC. XML-RPC resulta más simple para ejemplos básicos, mientras que gRPC ofrece una estructura más formal mediante archivos `.proto` y es más adecuado para aplicaciones distribuidas más completas.
```

# Laboratorio 10.1 - MQTT y Pydantic

## Alumno
- Pacara Ponciano Jose Miguel

## Ejecución

## Instalar dependencias:

pip install paho-mqtt pydantic

## Ejecutar suscriptor:

python subscriber_reto.py

## Ejecutar publicador:

python publisher_reto.py

## Cuestionario:
1. Pregunta Critica

¿Por qué no es viable utilizar una arquitectura síncrona HTTP REST para interconectar miles de sensores industriales que reportan datos cada pocos segundos?

No sería viable porque cada sensor tendría que enviar solicitudes constantemente al servidor mediante HTTP. Si existen miles de sensores reportando información cada pocos segundos, el servidor tendría que atender una gran cantidad de peticiones al mismo tiempo, consumiendo muchos recursos como memoria, procesador y conexiones.

Además, HTTP genera más tráfico debido a que sus cabeceras son más grandes. En cambio, MQTT fue diseñado para dispositivos IoT y utiliza paquetes mucho más pequeños, lo que reduce el uso de la red.

Por estas razones, MQTT resulta más adecuado para sistemas industriales, ya que permite una comunicación más eficiente y escalable mediante el modelo Publicador-Suscriptor, donde los sensores envían datos al broker sin conectarse directamente con cada receptor.

2. Pregunta Práctica

¿En qué escenarios es imperativo utilizar QoS 2 en lugar de QoS 0?

QoS 2 debe utilizarse cuando es muy importante que un mensaje llegue exactamente una vez y no pueda perderse ni duplicarse.

Por ejemplo:

Transferencias bancarias.
Registro de pagos.
Facturación electrónica.
Sistemas de seguridad industrial.
Control de inventarios de medicamentos.

En estos casos, un mensaje duplicado o perdido podría generar errores importantes.

Por otro lado, QoS 0 puede utilizarse en aplicaciones donde perder alguna lectura ocasional no representa un problema grave, como sensores de temperatura, humedad o monitoreo ambiental.

3. Reflexión Ética y RSU

¿Cómo contribuye MQTT a la sostenibilidad tecnológica de las regiones rurales del Perú?

MQTT contribuye a la sostenibilidad porque utiliza menos ancho de banda y menos recursos para transmitir información. Esto permite que los dispositivos consuman menos energía y funcionen mejor incluso con conexiones lentas o inestables.

En muchas zonas rurales del Perú la conectividad es limitada, por lo que un protocolo ligero como MQTT facilita implementar soluciones de monitoreo agrícola, ambiental o de cadena de frío sin requerir una infraestructura costosa.

Además, al reducir el tráfico de datos y el procesamiento necesario en los servidores, también disminuye el consumo energético y el impacto ambiental de los sistemas tecnológicos.

Conclusión

En este laboratorio aprendí a utilizar MQTT para la comunicación entre dispositivos IoT mediante el modelo Publicador-Suscriptor. También utilicé Pydantic para validar los datos recibidos y detectar errores antes de procesarlos. Gracias a las pruebas realizadas, pude comprobar que MQTT es una alternativa más eficiente que HTTP para aplicaciones industriales, ya que consume menos recursos y permite una comunicación más escalable y confiable.
import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PUERTO = 1883

def conectar_mqtt():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    print(f"Conectando al broker {BROKER}...")
    client.connect(BROKER, PUERTO, 60)

    return client


def main():
    cliente = conectar_mqtt()
    cliente.loop_start()

    camaras = [1, 2]

    try:
        while True:

            camara = random.choice(camaras)

            # Fallas intencionales
            probabilidad = random.randint(1, 10)

            if probabilidad == 1:
                temperatura = 999          # fuera de rango
            elif probabilidad == 2:
                temperatura = "ERROR"      # tipo incorrecto
            else:
                temperatura = round(
                    random.uniform(-2.0, 8.0),
                    2
                )

            datos_sensor = {
                "sensor_id": camara,
                "timestamp": time.time(),
                "valor": temperatura,
                "unidad": "Celsius"
            }

            mensaje = json.dumps(datos_sensor)

            topico = (
                f"unmsm/callao/camara/"
                f"{camara}/telemetria"
            )

            info = cliente.publish(
                topico,
                mensaje,
                qos=1
            )

            info.wait_for_publish()

            print(
                f"[PUBLISHER] {topico}: {mensaje}"
            )

            time.sleep(3)

    except KeyboardInterrupt:
        print("\nDeteniendo publicador...")

    finally:
        cliente.loop_stop()
        cliente.disconnect()


if __name__ == "__main__":
    main()
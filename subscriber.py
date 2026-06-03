import json
from datetime import datetime

import paho.mqtt.client as mqtt

from pydantic import (
    BaseModel,
    Field,
    ValidationError
)

BROKER = "broker.hivemq.com"
PUERTO = 1883

TOPICO = "unmsm/callao/camara/+/telemetria"


class LecturaSensor(BaseModel):
    sensor_id: int
    timestamp: float
    valor: float = Field(
        ...,
        ge=-50,
        le=100
    )
    unidad: str


def on_connect(
    client,
    userdata,
    flags,
    rc,
    properties
):
    if rc == 0:
        print("Conectado al broker MQTT")

        client.subscribe(TOPICO)

        print(
            f"Suscrito a: {TOPICO}"
        )

    else:
        print(
            f"Error de conexión: {rc}"
        )


def on_message(
    client,
    userdata,
    msg
):
    raw_payload = msg.payload.decode()

    print(
        f"\nMensaje recibido: {msg.topic}"
    )

    try:

        datos_json = json.loads(
            raw_payload
        )

        lectura = LecturaSensor(
            **datos_json
        )

        print(
            f"Camara {lectura.sensor_id}"
        )

        print(
            f"Temperatura: "
            f"{lectura.valor} "
            f"{lectura.unidad}"
        )

        # Alerta de cadena de frío
        if lectura.valor > 5:
            print(
                f"[PELIGRO] "
                f"¡Pérdida de cadena "
                f"de frío en Cámara "
                f"{lectura.sensor_id}!"
            )

    except (
        ValidationError,
        json.JSONDecodeError
    ) as e:

        print(
            "[ERROR] Datos descartados"
        )

        with open(
            "log_errores.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"{datetime.now()} "
                f"- {str(e)}\n\n"
            )


def main():

    cliente = mqtt.Client(
        callback_api_version=
        mqtt.CallbackAPIVersion.VERSION2
    )

    cliente.on_connect = on_connect
    cliente.on_message = on_message

    cliente.connect(
        BROKER,
        PUERTO,
        60
    )

    cliente.loop_forever()


if __name__ == "__main__":
    main()
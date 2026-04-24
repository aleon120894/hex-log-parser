
def is_mqtt(data: bytes) -> bool:

    if not data:
        return False
    packet_type = data[0] >> 4
    return packet_type in {1, 3, 8}  # CONNECT, PUBLISH, SUBSCRIBE

def decode_mqtt(data: bytes) -> dict:

    if len(data) < 2:
        return {"error": "Invalid MQTT packet"}

    packet_type = data[0] >> 4

    # Remaining Length (1 byte)
    remaining_length = data[1]
    result = {
        "protocol": "MQTT",
        "type": _get_packet_type(packet_type),
        "length": remaining_length
    }
    if packet_type == 3:
        return _parse_publish(data, result)

    return result

def _get_packet_type(packet_type: int) -> str:
    types = {
        1: "CONNECT",
        3: "PUBLISH",
        8: "SUBSCRIBE"
    }
    return types.get(packet_type, "UNKNOWN")

def _parse_publish(data: bytes, result: dict) -> dict:
    try:
        # topic length (2 байти)
        topic_len = (data[2] << 8) | data[3]

        topic_start = 4
        topic_end = topic_start + topic_len

        topic = data[topic_start:topic_end].decode("utf-8", errors="ignore")

        payload = data[topic_end:].decode("utf-8", errors="ignore")

        result.update({
            "topic": topic,
            "payload": payload
        })

        return result

    except Exception:
        result["error"] = "Failed to parse PUBLISH packet"
        return result

from parser.protocols.http import is_http, decode_http
from parser.protocols.redis import is_redis, decode_redis
from parser.protocols.mqtt import is_mqtt, decode_mqtt
from parser.protocols.modbus import is_modbus, decode_modbus

def decode_packets(hex_lines):
    results = []

    for line in hex_lines:
        try:
            raw_bytes = bytes.fromhex(line)
            decoded = decode_data(raw_bytes)
            results.append(decoded)

        except ValueError:
            results.append({
                "error": "Invalid HEX",
                "raw": line
            })

    return results

def decode_data(data: bytes) -> dict:
    if is_http(data):
        return decode_http(data)

    if is_redis(data):
        return decode_redis(data)

    if is_mqtt(data):
        return decode_mqtt(data)

    if is_modbus(data):
        return decode_modbus(data)

    return {
        "protocol": "UNKNOWN",
        "raw": data.hex()
    }
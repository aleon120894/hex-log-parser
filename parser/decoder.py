from parser.protocols.http import is_http, decode_http
from parser.protocols.redis import is_redis, decode_redis


def decode_data(data: bytes) -> dict:
    if is_http(data):
        return decode_http(data)

    if is_redis(data):
        return decode_redis(data)

    return {
        "protocol": "UNKNOWN",
        "raw": data.hex()
    }
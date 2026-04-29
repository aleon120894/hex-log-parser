

def is_modbus(data: bytes) -> bool:
    if len(data) < 8:
        return False

    # Protocol ID for Modbus TCP = 0
    protocol_id = (data[2] << 8) | data[3]
    return protocol_id == 0

def decode_modbus(data: bytes) -> dict:
    if len(data) < 8:
        return {"error": "Invalid Modbus packet"}

    try:
        transaction_id = (data[0] << 8) | data[1]
        protocol_id = (data[2] << 8) | data[3]
        length = (data[4] << 8) | data[5]
        unit_id = data[6]
        function_code = data[7]

        result = {
            "protocol": "MODBUS",
            "length": length,
            "transaction_id": transaction_id,
            "protocol_id": protocol_id,
            "unit_id": unit_id,
            "function": _get_function_name(function_code),
            "function_code": function_code
        }

        # simple data parsing (for Read Holding Registers)
        if function_code == 0x03 and len(data) >= 12:
            start_address = (data[8] << 8) | data[9]
            quantity = (data[10] << 8) | data[11]

            result.update({
                "start_address": start_address,
                "quantity": quantity
            })

        return result

    except Exception:
        return {"error": "Failed to parse Modbus packet"}

def _get_function_name(code: int) -> str:
    mapping = {
        0x01: "Read Coils",
        0x03: "Read Holding Registers",
        0x06: "Write Single Register"
    }
    return mapping.get(code, "UNKNOWN")


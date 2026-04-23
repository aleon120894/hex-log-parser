

def is_redis(data: bytes) -> bool:
    return data.startswith(b"*") or data.startswith(b"+")


def decode_redis(data: bytes) -> dict:
    try:
        text = data.decode("utf-8", errors="ignore")
    except Exception:
        return {"error": "Failed to decode Redis data"}

    lines = text.split("\r\n")
    result = []

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("*"):  # array
            count = int(line[1:])
            items = []
            i += 1

            for _ in range(count):
                if i >= len(lines):
                    break

                if lines[i].startswith("$"):  # bulk string
                    length = int(lines[i][1:])
                    i += 1
                    if i < len(lines):
                        items.append(lines[i])
                i += 1

            result.append(items)

        elif line.startswith("+"):  # simple string
            result.append(line[1:])
            i += 1

        else:
            i += 1

    return {
        "protocol": "REDIS",
        "commands": result
    }

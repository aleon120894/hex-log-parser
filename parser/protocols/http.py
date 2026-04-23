

def parse_request(lines):
    try:
        method, path, version = lines[0].split()
    except ValueError:
        return {"error": "Invalid request line"}

    headers = {}
    body = ""
    is_body = False

    for line in lines[1:]:
        if line == "":
            is_body = True
            continue

        if not is_body:
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()
        else:
            body += line

    return {
        "type": "request",
        "method": method,
        "path": path,
        "version": version,
        "headers": headers,
        "body": body
    }

def decode_http(data: bytes):
    try:
        text = data.decode("utf-8", errors="ignore")
    except Exception:
        return {"error": "Failed to decode bytes"}

    lines = text.split("\r\n")

    if not lines:
        return {"error": "Empty data"}

    first_line = lines[0]

    # визначаємо request чи response
    if first_line.startswith("HTTP/"):
        return parse_response(lines)
    else:
        return parse_request(lines)

def is_http(data: bytes):
    return data.startswith(b"GET") or \
           data.startswith(b"POST") or \
           data.startswith(b"PUT") or \
           data.startswith(b"DELETE") or \
           data.startswith(b"HTTP/")
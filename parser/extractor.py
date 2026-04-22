import re


HEX_PATTERN = r'([0-9A-Fa-f]{2}\s)+'

def extract_hex_lines(lines):

    result = []
    for line in lines:
        match = re.search(HEX_PATTERN, line)
        if match:
            result.append(match.group().strip())
    return result

from parser.reader import read_log
from parser.extractor import extract_hex_lines
from parser.decoder import decode_packets

def main():
    lines = read_log("data/sample.log")
    hex_lines = extract_hex_lines(lines)
    packets = decode_packets(hex_lines)

    for p in packets:
        print(p)

if __name__ == "__main__":
    main()


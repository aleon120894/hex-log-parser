from parser.reader import read_log
from parser.extractor import extract_hex_lines
from parser.decoder import decode_data, decode_packets
import argparse
import os
import json


def parse_args():
    parser = argparse.ArgumentParser(description="HEX log parser")
    parser.add_argument("--file", required=True, help="Path to log file")
    return parser.parse_args()


def main():
    args = parse_args()

    if not os.path.exists(args.file):
        raise FileNotFoundError(f"File not found: {args.file}")

    lines = read_log(args.file)
    hex_lines = extract_hex_lines(lines)
    packets = decode_packets(hex_lines)

    for p in packets:
        print(json.dumps(p, indent=2))


if __name__ == "__main__":
    main()

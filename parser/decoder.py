from parser.models import Packet


def decode_packets(hex_lines):

    packets = []
    for line in hex_lines:
        raw_bytes = bytes.fromhex(line)
        packet = Packet(raw_bytes)
        packets.append(packet)
    return packets

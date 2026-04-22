class Packet:

    def __init__(self, raw_bytes):

        self.raw = raw_bytes
        self.header = raw_bytes[:2]
        
        self.payload = raw_bytes[2:-1]
        self.checksum = raw_bytes[-1]

    def __repr__(self):
        return f"Packet(header={self.header}, payload={self.payload}, checksum={self.checksum})"

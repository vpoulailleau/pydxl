class Dynamixel:
    def __init__(self, identifier, serial_link):
        self.identifier = identifier
        self.serial_link = serial_link

    @property
    def address_map(self):
        return {}

    def ping(self):
        return self.serial_link.ping(self.identifier)

    def write(self, address, value, size):
        self.serial_link.write_bytes(self.identifier, address, value, size)

    def read(self, address, size):
        return self.serial_link.read_bytes(self.identifier, address, size)

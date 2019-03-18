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

    def __getattr__(self, name):
        reg = self.address_map.get(name)
        if reg:
            return 1  # TODO
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        reg = self.address_map.get(name)
        if reg and reg.write:
            self.write(reg.address, value, reg.size)
        else:
            super().__setattr__(name, value)

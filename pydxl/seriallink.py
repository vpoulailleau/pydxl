from pydxl import (
    DynamixelCommunicationException,
    DynamixelFailedOpeningPort,
    PortHandler,
)
from pydxl.protocol1 import PacketHandler as PacketHandler1

# TODO from dynamixel.protocol2 import PacketHandler as PacketHandler2


class SerialLink:
    def __init__(
        self, device="/dev/ttyUSB0", baudrate=1_000_000, protocol_version=1.0
    ):
        self.port_handler = PortHandler(device, baudrate)
        if int(10 * protocol_version) == 10:
            self.packet_handler = PacketHandler1(self.port_handler)
        else:
            self.packet_handler = PacketHandler2(self.port_handler)

    def close(self):
        self.port_handler.close()

    def ping(self, identifier):
        self.packet_handler.ping(identifier)

    def write_bytes(self, identifier, address, data, size):
        self.packet_handler.write_bytes(identifier, address, data, size)

    def read_bytes(self, identifier, address, size):
        return self.packet_handler.read_bytes(identifier, address, size)

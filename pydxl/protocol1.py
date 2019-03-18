import time

from pydxl import DynamixelCommunicationException, Packet

BROADCAST_ID = 254

# TODO
INST_READ = 2
INST_REG_WRITE = 4
INST_ACTION = 5
INST_FACTORY_RESET = 6
INST_CLEAR = 16


class PacketHandler:
    def __init__(self, port):
        self.port = port

    def write(self, packet):
        """Write a packet with the port handler."""
        packet.write_checksum()
        nb_written_bytes = self.port.write(packet)
        if nb_written_bytes != packet.total_length:
            raise DynamixelCommunicationException(
                "Problem in the number of sent bytes "
                f"({nb_written_bytes} out of {packet.total_length})"
            )

    def read(self):
        """Read a packet with the port handler."""
        # TODO check error code in packet.error
        data = []
        length_to_read = 6  # minimum packet size
        while True:
            data.extend(self.port.read(length_to_read - len(data)))

            header_pos = len(data)
            for i in range(len(data) - 1):
                if data[i] == 255 and data[i + 1] == 255:
                    # found header
                    header_pos = i
                    break
            else:
                continue  # header not found read more data
            if header_pos:
                data = data[header_pos:]

            packet = Packet.from_data(data)
            if packet.identifier >= BROADCAST_ID or packet.error > 127:
                del data[0]  # invalid packet, continue the reception
                continue

            length_to_read = packet.total_length
            if length_to_read == len(data):
                return packet

            time.sleep(0.03)

    def wait_ack(self, identifier):
        while True:
            self.port.set_timeout_for_length(8)
            response = self.read()
            if identifier == response.identifier:
                return response

    def write_bytes(self, identifier, address, data, size):
        data = int(data)
        if size == 1:
            data_write = [data]
        elif size == 2:
            data_write = [data & 0xFF, (data >> 8) & 0xFF]
        elif size == 4:
            data_write = [
                data & 0xFF,
                (data >> 8) & 0xFF,
                (data >> 16) & 0xFF,
                (data >> 24) & 0xFF,
            ]
        else:
            raise DynamixelCommunicationException("Unsupported size of data")

        packet = Packet(length=7 + len(data_write))
        packet.identifier = identifier
        packet.instruction = 3
        packet.parameter0 = address
        packet.payload = data_write
        self.write(packet)
        self.wait_ack(identifier)

    def read_bytes(self, identifier, address, size):
        packet = Packet(length=8)
        packet.identifier = identifier
        packet.instruction = 2
        packet.parameter0 = address
        packet.parameter1 = size
        self.write(packet)
        response = self.wait_ack(identifier)
        if size == 1:
            data = int(response.data[5])
        elif size == 2:
            data = int(response.data[5]) + (int(response.data[6]) << 8)
        elif size == 4:
            data = (
                int(response.data[5])
                + (int(response.data[6]) << 8)
                + (int(response.data[7]) << 16)
                + (int(response.data[8]) << 24)
            )
        return data

    def ping(self, identifier):
        if identifier >= BROADCAST_ID:
            raise DynamixelCommunicationException(
                f"Invalid identifier: {identifier}"
            )

        packet = Packet(length=6)
        packet.identifier = identifier
        packet.instruction = 1
        self.write(packet)
        self.wait_ack(identifier)

from textwrap import dedent

from pydxl import DynamixelMalFormedPacket


class Packet:
    def __init__(self, length):
        if length <= 4 or length > 250:
            raise DynamixelMalFormedPacket(
                f"Not allowed size of packet: {length}"
            )
        self.data = [0] * length
        self.data[0] = 255
        self.data[1] = 255
        self.data[3] = length - 4

    @classmethod
    def from_data(cls, data):
        packet = cls(len(data))
        packet.data = data
        if len(data) == packet.total_length:
            if not packet._check_checksum():
                raise DynamixelMalFormedPacket("Invalid checksum")
        return packet

    def __repr__(self):
        return dedent(
            f"""
            Packet
            | ID: {self.identifier}
            | instruction: {self.instruction}
            | paramater0: {self.parameter0}
            | payload: {self.payload}
            | length: {self.length}
            | error: {self.error}
            | raw_data: {self.data}
            """
        )

    @property
    def identifier(self):
        return self.data[2]

    @identifier.setter
    def identifier(self, value):
        self.data[2] = value

    @property
    def length(self):
        return self.data[3]

    @property
    def error(self):
        return self.data[4]

    @property
    def total_length(self):
        return self.length + 4

    @property
    def instruction(self):
        return self.data[4]

    @instruction.setter
    def instruction(self, value):
        self.data[4] = value

    @property
    def parameter0(self):
        return self.data[5]

    @parameter0.setter
    def parameter0(self, value):
        self.data[5] = value

    @property
    def parameter1(self):
        return self.data[6]

    @parameter1.setter
    def parameter1(self, value):
        self.data[6] = value

    @property
    def payload(self):
        return self.data[6 : self.total_length - 1]

    @payload.setter
    def payload(self, data):
        for index, value in enumerate(data):
            self.data[6 + index] = value

    def _compute_checksum(self):
        checksum = 0
        # compute checksum of everything except header, checksum
        for word in self.data[2 : self.total_length - 1]:
            checksum += word
        return ~checksum & 0xFF

    def write_checksum(self):
        self.data[self.total_length - 1] = self._compute_checksum()

    def _check_checksum(self):
        return self.data[self.total_length - 1] == self._compute_checksum()

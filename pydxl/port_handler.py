import time

import serial

from pydxl import DynamixelCommunicationException, DynamixelFailedOpeningPort


class PortHandler:
    def __init__(self, device="/dev/ttyUSB0", baudrate=1_000_000):
        self.device = device
        self.serial = None
        self._baudrate = baudrate
        self.open()
        self.packet_start_time = self._time()
        self.packet_timeout = 0

    def close(self):
        self.serial.close()

    def write(self, packet):
        nb_written_bytes = self.serial.write(packet.data)
        self.serial.flush()
        return nb_written_bytes

    def read(self, length):
        if self._time() >= self.packet_start_time + self.packet_timeout:
            raise DynamixelCommunicationException("timeout")
        return self.serial.read(length)

    @property
    def baudrate(self):
        return self._baudrate

    @baudrate.setter
    def baudrate(self, value):
        if value == self._baudrate:
            return  # already set to this baudrate
        if value not in (
            9600,
            19200,
            38400,
            57600,
            115_200,
            230_400,
            460_800,
            500_000,
            576_000,
            921_600,
            1_000_000,
            1_152_000,
            2_000_000,
            2_500_000,
            3_000_000,
            3_500_000,
            4_000_000,
        ):
            raise DynamixelFailedOpeningPort(f"Invalid baudrate: {value} bps")

        self.close()
        self.open()

    def open(self):
        self.serial = serial.Serial(
            port=self.device,
            baudrate=self.baudrate,
            bytesize=serial.EIGHTBITS,
            timeout=0,
        )
        if not self.serial.is_open:
            raise DynamixelFailedOpeningPort(f"Failed opening {device}")

    @staticmethod
    def _time():
        """Return time in milliseconds."""
        return round(time.time() * 1_000_000_000) / 1_000_000.0

    def set_timeout_for_length(self, length):
        tx_time_per_byte = (1000.0 / self.baudrate) * 10000.0
        self.packet_timeout = tx_time_per_byte * length + 34.0
        self.packet_start_time = self._time()

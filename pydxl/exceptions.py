class DynamixelException(Exception):
    pass


class DynamixelFailedOpeningPort(DynamixelException):
    pass


class DynamixelFailedSettingBaudrate(DynamixelException):
    pass


class DynamixelCommunicationException(DynamixelException):
    pass


class DynamixelMalFormedPacket(DynamixelException):
    pass

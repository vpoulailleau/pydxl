from pydxl.dynamixel import Dynamixel
from pydxl.register import Register


class Mx28(Dynamixel):
    torque_enable = Register(address=24, write=True, size=1)
    led = Register(address=25, write=True, size=1)
    goal_position = Register(address=30, write=True, size=2)

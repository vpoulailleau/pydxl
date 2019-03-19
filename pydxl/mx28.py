"""MX-28 servo usage."""
from pydxl.dynamixel import Dynamixel
from pydxl.register import Register


class Mx28(Dynamixel):
    """Class for MX-28 servo."""

    # http://emanual.robotis.com/docs/en/dxl/mx/
    # mx-28/#control-table-of-eeprom-area
    model_number = Register(address=0, size=2)
    firmware_version = Register(address=2)
    id_ = Register(address=3, write=True)
    baud_rate = Register(address=4, write=True)
    return_delay_time = Register(address=5, write=True)
    cw_angle_limit = Register(address=6, write=True, size=2)
    ccw_angle_limit = Register(address=8, write=True, size=2)
    temperature_limit = Register(address=11, write=True)
    min_voltage_limit = Register(address=12, write=True)
    max_voltage_limit = Register(address=13, write=True)
    max_torque = Register(address=14, write=True, size=2)
    status_return_level = Register(address=16, write=True)
    alarm_led = Register(address=17, write=True)
    shutdown = Register(address=18, write=True)
    multi_turn_offset = Register(address=20, write=True, size=2)
    resolution_divider = Register(address=22, write=True)

    # http://emanual.robotis.com/docs/en/dxl/mx/
    # mx-28/#control-table-of-ram-area
    torque_enable = Register(address=24, write=True)
    led = Register(address=25, write=True)
    d_gain = Register(address=26, write=True)
    i_gain = Register(address=27, write=True)
    p_gain = Register(address=28, write=True)
    goal_position = Register(address=30, write=True, size=2)
    moving_speed = Register(address=32, write=True, size=2)
    torque_limit = Register(address=34, write=True, size=2)
    present_position = Register(address=36, size=2)
    present_speed = Register(address=38, size=2)
    present_load = Register(address=40, size=2)
    present_voltage = Register(address=42)
    present_temperature = Register(address=43)
    registered = Register(address=44)
    moving = Register(address=46)
    lock = Register(address=47, write=True)
    punch = Register(address=48, write=True, size=2)
    realtime_tick = Register(address=50, size=2)
    goal_acceleration = Register(address=73, write=True)

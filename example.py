import time

from pydxl import Mx28, SerialLink

link = SerialLink(
    device="/dev/ttyUSB0", baudrate=1_000_000, protocol_version=1.0
)
shoulder1 = Mx28(identifier=1, serial_link=link)
shoulder2 = Mx28(identifier=2, serial_link=link)
elbow = Mx28(identifier=3, serial_link=link)

shoulder1.ping()
shoulder1.led = True

shoulder2.ping()
shoulder2.led = True

elbow.ping()
elbow.led = True


shoulder1.torque_enable = True
shoulder2.torque_enable = True
elbow.torque_enable = True

shoulder1.goal_position = 2000
shoulder2.goal_position = 2500
elbow.goal_position = 3000
time.sleep(3)

shoulder1.goal_position = 1500
shoulder2.goal_position = 2000

for _ in range(5):
    elbow.goal_position = 1500
    time.sleep(0.5)
    elbow.goal_position = 2500
    time.sleep(0.5)

elbow.goal_position = 3000
shoulder1.torque_enable = False
shoulder2.torque_enable = False
elbow.torque_enable = False

link.close()

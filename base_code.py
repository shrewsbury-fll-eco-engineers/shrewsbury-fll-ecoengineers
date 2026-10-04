from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

right_motor = Motor(Port.F,positive_direction=Direction.CLOCKWISE)
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
lam=Motor(Port.A,positive_direction=Direction.CLOCKWISE)
ram=Motor(Port.E,positive_direction=Direction.CLOCKWISE)
driving_base=DriveBase(left_motor,right_motor,wheel_diameter=43.2,axle_track=72.0)

driving_base.use_gyro(True)
#driving_base.settings(200, 400, 120, 240)
driving_base.settings(150, 200, 90, 180)
driving_base.straight(520)
print("one")
wait(100)
driving_base.turn (-20)
#print("three")
#wait(500)
#print("four")
driving_base.straight(75)
#print("five")
lam.run_angle(90,90)
#print("six")
#wait(100)
lam.run_angle(90,-90)
driving_base.straight(-74)
driving_base.turn(20)
wait(100)
driving_base.straight(-520)

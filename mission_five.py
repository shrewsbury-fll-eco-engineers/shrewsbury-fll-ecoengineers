
################################################################################
# mission_five.py
#
# Description: Reaching Roots mission
# Author(s): [Your Name(s)]
# Date: 2026-10-17
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
################################################################################

from robot import robot
from pybricks.tools import wait


def mission_five(r: robot):
    print("Running Reaching Roots Mission")

    # Drive toward the mission model
    #r.robot.straight(690)
    #r.robot.turn(89)

    # Activate the ram mechanism
    #r.ram.run_angle(300, -40)

    # Approach the roots
    #r.robot.straight(475)

    # Operate the attachment to extend the roots
    r.robot.use_gyro(True)
    r.robot.settings(straight_speed=300, straight_acceleration=400, turn_rate=120, turn_acceleration=240)
    r.ram.run_angle(1000, 120)
    r.robot.straight(750)
    r.robot.reset(0, 0)
    wait(100)
    r.robot.settings(straight_speed=300, straight_acceleration=400, turn_rate=110, turn_acceleration=220)#40 is working slow speed
    wait(100)
    r.ram.run_angle(40, -70)
    wait(100)
    r.robot.straight(128)
    wait(100)
    r.robot.turn(-25)
    wait(100)
    r.robot.straight(-128)#1st lift and reverse 
    r.robot.reset(0, 0)
    r.robot.turn(15)
    r.robot.straight(-42)
    r.ram.run_angle(40, 70)
    r.robot.straight(22)
    r.ram.run_angle(40, -90)
    r.robot.straight(185)
    r.robot.turn(-20)
    r.robot.settings(straight_speed=300, straight_acceleration=400, turn_rate=120, turn_acceleration=240)
    wait(100)
    #r.robot.turn(-25)
    #wait(100)
    r.robot.straight(-200)
    r.robot.turn(50)
    r.robot.straight(-540)
    r.robot.turn(90)
    r.robot.straight(-300)
    # r.robot.straight(-100)
    # r.ram.run_angle(300, 180)
    #r.robot.straight(60)
    #r.ram.run_angle(300, -150)
    #r.robot.straight(-100)
    #r.ram.run_angle(300, 120)
   # r.robot.straight(60)
    #r.ram.run_angle(300, -150)
   # r.robot.straight(-745)
    #r.ram.run_angle(10000, 360)
    #r.ram.run_angle(10000, 360)

    # Activate the secondary attachment if required
    #r.lam.run_angle(30, 75)
    #wait(1000)
    #r.lam.run_angle(30, -70)

    # Back away from the mission model
    #r.robot.straight(-475)
    #r.robot.turn(-90)
    #r.robot.straight(-690)


################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

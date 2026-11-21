################################################################################
# mission_three.py
#
# Description:
# [Describe What your mission does here]
#
# Author(s): [Your Name(s)]
# Date: [YYYY-MM-DD]
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################

from robot import robot, STRAIGHT_SPEED, TURN_RATE
from pybricks.tools import wait

def mission_three(r: robot):
    print("Running Mission 3")
    r.robot.use_gyro(True)
    r.robot.settings(straight_speed=400, straight_acceleration=500, turn_rate=120, turn_acceleration=240)
    r.robot.straight(450)
    r.robot.straight(-100)
    r.robot.straight(100)
    r.robot.turn(-7.5)
    r.robot.straight(-100)
    r.robot.straight(100)
    r.robot.turn(10)
    r.robot.straight(-100)
    r.robot.straight(100)
    r.robot.straight(-700)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()


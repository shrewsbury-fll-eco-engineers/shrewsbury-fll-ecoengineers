################################################################################
# mission_one.py
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
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_one(r: robot):
    print("Running Mission 1")
    # Your code goes here...
    # Sample Code: Run attachment motors and drive motors
    r.robot.settings(200,400,120,240)
    r.robot.straight(400)
    r.robot.turn(-10)
    r.robot.straight(220)
    r.robot.turn(-10)
    r.robot.turn(-15)
    r.robot.straight(-30)
    r.robot.turn(40)
    r.robot.straight(-750)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

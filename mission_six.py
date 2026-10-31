################################################################################
# mission_six.py
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

def mission_six(r: robot):
    print("Running Mission 6")
    r.robot.settings(400,800,120,240)
    r.robot.straight(150)
    r.robot.turn(-50)
    r.robot.straight(590)
    r.robot.turn(-40)
    r.robot.straight(100)
    r.robot.straight(-50)
    r.robot.turn(90)
    r.robot.straight(100)
    r.robot.turn(30)
    r.robot.straight(150)
    r.robot.settings(90,180,120,240)
    r.robot.straight(150)
    r.robot.settings(700,1400,120,240)
    r.robot.straight(-50)
    r.robot.turn(-67)
    r.robot.straight(-500)
    r.robot.turn(180)
    r.robot.straight(500)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

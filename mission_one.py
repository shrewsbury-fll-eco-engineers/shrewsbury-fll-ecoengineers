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
    r.robot.settings(400,800,120,240)
    r.lam.run_angle(300, 120)
    r.robot.straight(451)
    r.robot.turn(-10)    
    r.robot.straight(220)
    r.robot.turn(-25)

    r.robot.settings(600,1200,120,240)
    r.robot.straight(-30)
    r.robot.turn(40)
    r.robot.straight(-600)

    r.robot.settings(400,800, 120, 240)
    r.robot.turn(-45)
    r.robot.straight(330)
    r.lam.run_angle(300,-90)
    r.robot.straight(-1000)


################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

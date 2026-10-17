################################################################################
# mission_four.py
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

def mission_four(r: robot):
    print("Running Mission 4")
    # Your code goes here...
    # Sample code: Test the speaker
    r.robot.settings(straight_speed=200, straight_acceleration=400, turn_rate=120, turn_acceleration=240)
    r.robot.straight(740)
    r.robot.turn(-26.7)
    r.lam.run_time(20,1000)
    r.robot.straight(37)
    #r.robot.drive(0,10)
    r.lam.run_time(80,1000)
    r.robot.straight(-37)
    r.robot.turn(26.7)
    r.robot.straight(-740)
    r.lam.run_time(-80,1000)
    #r.robot.stop()
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

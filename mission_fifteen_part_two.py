################################################################################
# mission_fifteen_part_two.py
#
# Description:
# Mission 15 part two - the other side, starting from the other home base.
#
# Author(s): [Your Name(s)]
# Date: 2026-10-03
# Version: 1.0
#
# Dependencies:
# - robot
# - pybricks.tools
#
################################################################################
from robot import robot
from pybricks.tools import wait, StopWatch

def mission_fifteen_part_two(r: robot):
    print("Running Mission 15 part 2")
    r.robot.straight(150)
    r.robot.turn(-50)
    r.robot.straight(590)
    r.robot.turn (-40)
    r.robot.straight(100)
    r.robot.straight(-50)
    r.robot.turn(50)
    r.robot.straight(-600)
    r.robot.turn(100)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

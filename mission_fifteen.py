################################################################################
# mission_fifteen.py
#
# Description:
# [Describe What your mission does here]
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

def mission_fifteen(r: robot):
    print("Running Mission 15")
    r.robot.straight(690)
    r.robot.turn (89)
    r.ram.run_angle(300, -40)
    r.robot.straight(475)
    r.ram.run_angle(300, 60)
    r.ram.run_angle(300, -45)
    r.lam.run_angle(30, 75)
    wait(1000)
    r.lam.run_angle(30,-70)
    r.robot.straight(-475)
    r.robot.turn(-90)
    r.robot.straight(-690)
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

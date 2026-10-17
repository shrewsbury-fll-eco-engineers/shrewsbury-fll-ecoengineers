
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
    r.robot.straight(690)
    r.robot.turn(89)

    # Activate the ram mechanism
    r.ram.run_angle(300, -40)

    # Approach the roots
    r.robot.straight(475)

    # Operate the attachment to extend the roots
    r.ram.run_angle(300, 60)
    r.ram.run_angle(300, -45)

    # Activate the secondary attachment if required
    r.lam.run_angle(30, 75)
    wait(1000)
    r.lam.run_angle(30, -70)

    # Back away from the mission model
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

################################################################################
# mission_seven.py
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
from robot import STRAIGHT_SPEED, TURN_RATE, robot

def mission_seven(r: robot):
    print("Running Mission 7")
    r.robot.settings(straight_speed=150, turn_rate=TURN_RATE)
    # Your code goes here...
    r.robot.straight(300)

    
    r.ram.run_time(-20,1000)
    r.robot.turn(7.5)
    r.robot.straight(50)
    r.ram.run_time(-20,1000)
    r.robot.straight(-150)
    r.ram.run_time(40,1000)
    r.robot.straight(-150)
    r.robot.turn(-14.7)
    r.robot.settings(straight_speed=400, turn_rate=TURN_RATE)
    r.robot.straight(660)

    r.lam.run_time(-150,2750)
    r.robot.straight(-200)
    r.lam.run_time(200,1000)
    r.robot.straight(-10000)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
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
    #r.robot.turn(-50)
    #r.robot.straight(590)
    #r.robot.turn(-40)
    #r.robot.straight(100)
    #r.robot.straight(-50)
    #r.robot.turn(90)
    #r.robot.straight(100)
    #r.robot.turn(30)
    #r.robot.straight(150)
    #r.robot.settings(70,140,120,240)
    #r.robot.straight(120)
    #r.robot.settings(700,1400,120,240)
    #r.robot.straight(-50)
    #r.robot.turn(-69)
    #r.robot.straight(-500)
    #r.robot.turn(160)
    #r.robot.straight(500)


    #New Code, mission was backward
    #mission 11
    r.robot.settings (400, 800, 120, 240)
    r.robot.straight(100)
    r.robot.turn(-50)
    r.robot.straight(500)
    #mission 15 (right side)
    r.ram.run_angle(300, -40)
    r.robot.straight(50)
    r.robot.turn(-38)
    r.robot.straight(5)
    r.ram.run_angle(300, 80)
    r.robot.straight(10)
    r.robot.straight(-20)
    r.robot.turn(-6)
    r.ram.run_angle(50, -95)
    r.robot.straight(10)
    r.robot.turn(-5)
    wait(1000)
    r.ram.run_angle(50, 50)
    r.robot.straight(-50)
    r.ram.run_angle(500, -130)
    #mission 6
    r.robot.straight(-10)
    r.robot.turn(70)
    r.robot.straight(120)
    r.robot.turn(35)
    r.robot.straight(165)
    r.robot.turn(35)
    r.robot.settings(70, 140, 120, 240)
    r.robot.straight(200)
    r.robot.settings(700,1400,120,240)
    r.robot.straight(-50)
    r.robot.turn(-80)
    r.robot.straight(-500)
    r.robot.turn(160)
    r.robot.straight(500)
    

# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
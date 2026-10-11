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

from robot import TURN_RATE, robot
from robot import STRAIGHT_SPEED, robot
from pybricks.tools import wait, StopWatch

# def mission_three(r: robot):
    #print("Running Mission 3")
    # Your code goes here...
    # Sample Code: Test running the attachment motor until stalled
    #r.robot.straight(1080)
    #r.robot.turn(-90)
    #r.robot.straight(97)
    #r.robot.turn(-90)
    
def mission_three(r: robot):
    print("Running Mission 3")
    drivebase = r.robot
    left_attachment = r.lam
    right_attachment = r.ram
    drivebase.settings(straight_speed=STRAIGHT_SPEED, turn_rate=TURN_RATE)
    left_attachment.stop()
    right_attachment.stop()

    drivebase.stop()
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.straight(492.4, wait=False)
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.stop()
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.straight(-70.1, wait=False)
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.stop()
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.straight(112.6, wait=False)
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
       wait(3)
    drivebase.stop()
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.straight(-306.4, wait=False)
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.stop()
    left_attachment.stop()
    right_attachment.stop()
    while not drivebase.done() or not left_attachment.done() or not right_attachment.done():
        wait(3)
    drivebase.stop()
    left_attachment.stop()
    right_attachment.stop()


################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()


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
    # Run as fast as the drive motors allow.
    # Read this hub's real motor speed limit (deg/s) instead of guessing,
    # and convert it to mm/s for the 56 mm wheels (pi * 56 / 360 mm per deg).
    motor_max_deg_s = r.ldm.control.limits()[0]
    top_speed = int(motor_max_deg_s * 3.14159 * 56 / 360)
    # Acceleration 2000 -> 3000 mm/s^2: reaching top speed sooner saves the
    # most time. If the wheels slip or the robot veers at the start,
    # lower this back toward 2000.
    r.robot.settings(straight_speed=top_speed, straight_acceleration=3000, turn_rate=120)
    print("Mission 4 top speed:", top_speed, "mm/s")

    # Distance 2300 mm (was 2000 before +300 mm). Timed so we can compare runs.
    timer = StopWatch()
    r.robot.straight(950)
    r.robot.arc(100, 180)
    r.robot.straight(-1000)

   # r.robot.straight(2300)
   # print("Mission 4 drive time:", timer.time(), "ms")
    #r.robot.drive(0,10)
    #r.ram.run_time(-270,5000)
    #r.robot.stop()
################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()

################################################################################
# menu.py
#
# Handles mission selection via the SPIKE Prime hub menu.
# Allows users to choose and execute predefined missions based on display
# orientation, ensuring intuitive navigation.
#
# Author: ECO Engineers
# Date: 2025-03-15
# Version: 1.0
#
# Dependencies:
# - robot (for accessing robot instance and display orientation)
# - pybricks.parameters (Side)
# - pybricks.tools (hub_menu for user selection)
# - mission_x.py files (each containing a specific mission routine)
#
# Functionality:
# - Dynamically adjusts menu order based on the hub’s display orientation.
# - Calls the appropriate mission function based on user selection.
#
################################################################################

from robot import robot
from pybricks.parameters import Side
from pybricks.tools import hub_menu, wait

def menu(r: robot):
    from mission_one import mission_one
    from mission_two import mission_two
    from mission_three import mission_three
    from mission_four import mission_four
    from mission_five import mission_five
    from mission_six import mission_six
    from mission_seven import mission_seven
    #from mission_eight import mission_eight
    #from mission_nine import mission_nine
    #from mission_fifteen import mission_fifteen
    #from mission_fifteen_part_two import mission_fifteen_part_two
    # Missions in run order: (menu label, function).
    # The menu opens on the first entry, and after each mission it moves
    # to the next one, so this list IS the match run order.
    # Match order: 7, 6, 4, 1, 5, 3. The rest stay reachable with the arrows.
    # Mission 12 is left out until it is ready (it used to be on the
    # menu but did nothing when selected, which wasted button presses).
    missions = [
        ("7", mission_seven),
        ("6", mission_six),
        ("4", mission_four),
        ("1", mission_one),
        ("5", mission_five),
        ("3", mission_three),
        #("2", mission_two),
        #("8", mission_eight),
        #("9", mission_nine),
        #(15, mission_fifteen),
        #(16, mission_fifteen_part_two),
    ]
    labels = [label for label, _ in missions]
    reversed_display = (
        r.display_orientation == Side.BOTTOM or r.display_orientation == Side.LEFT
    )

    # Stay in the menu instead of ending the program after one mission.
    # After a mission finishes, the NEXT mission is shown first, so the
    # usual run order needs only one center-button press per mission.
    # Use the arrows only to skip ahead or go back.
    start = 0
    while True:
        # Rotate so the mission we expect to run next is the first option.
        ordered = labels[start:] + labels[:start]
        # Flip the order when the hub is upside down / sideways so the
        # arrow selections still make sense.
        if reversed_display:
            ordered = [ordered[0]] + ordered[1:][::-1]

        selected = hub_menu(*ordered)

        index = labels.index(selected)
        try:
            missions[index][1](r)
        except SystemExit:
            # The center (stop) button raises SystemExit. Catch it so a
            # stopped mission returns to the menu (and still advances to
            # the next mission) instead of ending the whole program.
            print("Mission", selected, "stopped with center button")
            r.robot.stop()
            r.lam.stop()
            r.ram.stop()

        # Wait for the center button to be released so the press that
        # stopped the mission doesn't also select the next one.
        while r.hub.buttons.pressed():
            wait(10)

        # Default to the next mission; wrap back to the first at the end.
        start = (index + 1) % len(missions)

################################
# KEEP THIS AT THE END OF THE FILE
# This redirects to running main.
################################
if __name__ == "__main__":
    from main import main
    main()
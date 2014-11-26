"""
The  **** Stop! In the Name of Love! **** Python Capstone Project.

CSSE 120 - Introduction to Software Development (Robotics).
Fall term, 2013-2014.
Team members: Andrew, Anqi, Steve (all of them).

The primary author of this module is:  ENTIRE TEAM.

This module contains a CLASS for bundling SHARED data.
Your team can (and should) bundle things into classes sensibly.
"""
# TODO: Put the names of ALL team members in the above where indicated.

import m1  # @UnusedImport
import m2  # @UnusedImport
import m3  # @UnusedImport
import m4  # @UnusedImport
import new_create  # imports robot

def main():
    """ Runs the MAIN PROGRAM. """
    # Intended to be used when running the main (entire) program.
    print('Integration Testing of the MAIN PROGRAM:\n')


class Box_of_Fun_Toys_for_Robots(new_create.Create):
    # pass on the robo code
    """contains robo parts """

    def __init__(self, speed, time_value, port, angle):
        """ Initialize fields (instance variables). """
        # TODO: ADD     self.FOO = BLAH     HERE AS NEEDED.
        # gives us the robo code

        self.robot = None
        self.speed = speed
        self.port = port

        self.time_value = time_value
        self.angle = angle
        self.message = None

    def get_port(self):
        return self.port

    def get_speed(self):
        return self.speed

    def get_angle(self):
        return self.angle

    def get_time_value(self):
        return self.time_value

    def __repr__(self):
        """ Returns a string that represents this object. """
        return None

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

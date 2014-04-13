#===============================================================================
from subprocess import Popen, PIPE, STDOUT
#-------------------------------------------------------------------------------
class LEDSign():
    # Sign dimensions (to aid in text formatting).
    SCREEN_WIDTH = 96
    SCREEN_HEIGHT = 16
#-------------------------------------------------------------------------------
    def __init__(self, lowlevel_path):
        self.SCRIPT = '/'.join([lowlevel_path, 'lowlevel.pl'])
#-------------------------------------------------------------------------------
    def pic(self, data):
        draw = ['/usr/bin/perl', self.SCRIPT, '--type=pic']
        p = Popen(draw, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.communicate(input=data)[0]
#-------------------------------------------------------------------------------
class Array:
#-------------------------------------------------------------------------------
    def zero_one(self, data):
        zero_oned = ""
        for row in data:
            joined_row = "".join("{0}".format(n) for n in row)
            zero_oned += joined_row + "\n"
        return zero_oned
#===============================================================================

#===============================================================================
from sign import LEDSign, Array
from simplefont import sign_font
#-------------------------------------------------------------------------------
class SignClient:
    def __init__(self, glyphs_path, lowlevel_path):
        self.glyphs_path = glyphs_path
        self.lowlevel_path = lowlevel_path
#-------------------------------------------------------------------------------
    def send_text_to_sign(self, lines):
        font = sign_font(self.glyphs_path)

        matrix = font.render_multiline(
                    lines,
                    LEDSign.SCREEN_HEIGHT / 2,
                    {
                        "ignore_shift_h" : True,
                        "fixed_width" : LEDSign.SCREEN_WIDTH
                        }
                    )

        if not matrix:
            return False

        text_for_sign = Array().zero_one(matrix)

        # View matrix rendering of text
        #print text_for_sign

        # Send text to led sign
        LEDSign(self.lowlevel_path).pic(text_for_sign)
        return True
#===============================================================================

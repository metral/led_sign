#===============================================================================
from sign import LEDSign, Array
from simplefont import sign_font
#-------------------------------------------------------------------------------
class SignClient:
#-------------------------------------------------------------------------------
    def send_text_to_sign(self, lines):
        font = sign_font("<SOME_PATH>")

        text_for_sign = Array().zero_one(
                font.render_multiline(
                    lines,
                    8,
                    {
                        "ignore_shift_h" : True,
                        "distance" : 0,
                        "fixed_height" : LEDSign.SCREEN_HEIGHT,
                        "fixed_width" : LEDSign.SCREEN_WIDTH
                        }
                    )
                )

        # View matrix rendering of text
        #print text_for_sign

        # Send text to led sign
        LEDSign().pic(text_for_sign)
#===============================================================================

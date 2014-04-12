#===============================================================================
from sign import LEDSign, Array
from simplefont import sign_font
#-------------------------------------------------------------------------------
class SignClient:
#-------------------------------------------------------------------------------
    def send_text_to_sign(self, lines):
        font = sign_font()

        text_for_sign = Array().zero_one(
                font.render_multiline(
                    lines,
                    LEDSign.SCREEN_HEIGHT / 2,
                    {
                        "ignore_shift_h" : True,
                        "fixed_width" : LEDSign.SCREEN_WIDTH
                        }
                    )
                )

        # View matrix rendering of text
        #print text_for_sign

        # Send text to led sign
        LEDSign().pic(text_for_sign)
#===============================================================================

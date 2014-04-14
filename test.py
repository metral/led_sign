import os
from client import SignClient

multiline_test = []

top_line = "Python rocks!"
bottom_line = "Ruby is cool too :)"
multiline_test = [top_line, bottom_line]

pwd = os.path.dirname(os.path.realpath(__file__))
led_sign_path = '/'.join([pwd, 'led_sign']) 
glyphs_path = '/'.join([led_sign_path, 'glyphs'])

SignClient(glyphs_path, led_sign_path).send_text_to_sign(multiline_test)

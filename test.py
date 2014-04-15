import os
from client import SignClient

multiline_test = []

top_line = "Python rocks!"
bottom_line = "Ruby is cool too :)"
multiline_test = [top_line, bottom_line]

pwd = os.path.dirname(os.path.realpath(__file__))
glyphs_path = '/'.join(['glyphs'])

SignClient(glyphs_path, pwd).send_text_to_sign(multiline_test)

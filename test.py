from client import SignClient

multiline_test = []

top_line = "Python rocks!"
bottom_line = "Ruby is cool too :)"
multiline_test = [top_line, bottom_line]

SignClient().send_text_to_sign(multiline_test)

LED Sign
========

Description: Python fork of Ruby code: https://github.com/pshved/muni-led-sign/

LED Sign: http://www.brightledsigns.com/products/4_x16_LED_Mini_Desk_Sign-12972-0.html

File description:

* lowlevel.pl — Perl wrapper for Perl API interaction with the LED sign made available via the CPAN module: Device::MiniLED.
* font/*.simpleglyphs — Collection of custom font glyphs that allows for the composition of individual ASCII characters using binary data to turn on / off a specific LED.
* lib/simplefont.rb — Loads the custom font glyphs from font/*.simpleglyphs and renders the multiline text. It achieves the rendering by creating a single 16x96 matrix comprised of concatenated character glyphs for each character in the supplied strings for each of the top and bottom line of the LED sign.
* lib/sign.rb — Retrieves the rendering of the strings from lib/simplefont.rb and supplies it to lowlevel.pl API wrapper to write out to the sign.

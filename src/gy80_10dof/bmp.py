import Adafruit_Python_BMP.BMP085 as BMP0852

# Copyright (c) 2014 Adafruit Industries
# Author: Manuel Reilaender
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class BMP085(object):
    # TODO Modi static variables
    def __init__(self, mode, bus=1):
        """
        Constructor

        :param mode: String Can be ULTRALOWPOER, STANDARD, HIGHRES or ULTRAHIGHRES
        :param bus: int Optionally Busnumber
        """
        if isinstance(mode, basestring):
            if mode == "ULTRALOWPOWER":
                self.bmp085 = BMP0852.BMP085(BMP0852.BMP085_ULTRALOWPOWER)
            elif mode == "STANDARD":
                self.bmp085 = BMP0852.BMP085(BMP0852.BMP085_STANDARD)
            elif mode == "HIGHRES":
                self.bmp085 = BMP0852.BMP085(BMP0852.BMP085_HIGHRES)
            elif mode == "ULTRAHIGHRES":
                self.bmp085 = BMP0852.BMP085(BMP0852.BMP085_ULTRAHIGHRES)
            else:
                raise ValueError("Not basestring: Expected values doesn't match given value: " + mode)
        else:
            raise TypeError("Incompatible Types: Expected basestring given " + type(mode))

    def get_temperature(self):
        """
        Returns the Temperature in degrees Celsius

        :return: float
        """
        return self.bmp085.read_temperature()

    def get_pressure(self):
        """
        Returns the pressure in Pascals

        :return: long
        """
        return self.bmp085.read_pressure()

    def get_altitude(self):
        """
        Returns the altitude in meters

        :return: float
        """
        return self.bmp085.read_altitude()

    def get_sealevel_pressure(self):
        """
        Returns the pressure at sealevel when given a known altitude in

        :return: float
        """
        return self.bmp085.read_sealevel_pressure()
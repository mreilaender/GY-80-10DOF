from libhmc5883l import hmc5883l

'''
Copyright 2015 Manuel Reilaender

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


class HMC5883L(object):
    """
    Wrapper class for the HMC5883L using a library from Taur-Tech https://github.com/Taur-Tech/HMC5883L

    HMC5883L is an 3-Axis Magnetic Compass
    """

    def __init__(self, bus=1):
        """
        Constructor

        :param bus: int Optionally Busnumber Default is 1
        """
        self.hmc5883l = hmc5883l.HMC5883L(bus)

    def set_parameter(self, parameter, value):
        """
        Sets various parameters, documentation located at doc/

        :param parameter: str
        :param value: str
        :return:
        """
        self.hmc5883l.set_parameter(parameter, value)

    def get_xyz(self):
        """
        Returns a dictonary with 'x', 'y' and 'z' as keys.

        :return: dict
        """
        return self.hmc5883l.get_field_xyz()

    def get_x(self):
        """


        :return: float
        """
        return self.hmc5883l.get_field_x()

    def get_y(self):
        """


        :return: float
        """
        return self.hmc5883l.get_field_y()

    def get_z(self):
        """


        :return: float
        """
        return self.hmc5883l.get_field_z()
import l3g4200d as tmp
import smbus

# Copyright 2015 Manuel Reilaender

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

bus = smbus.SMBus(1)
test = tmp.L3G4200D(bus, 0x69, "asd")

#while True:
test.read_raw_data()
print "X: ", test.read_scaled_gyro_x()
print "Y: ", test.read_scaled_gyro_y()
print "Z: ", test.read_scaled_gyro_z()

class L3G4200D(object):
    """
    Wrapper class for the L3G4200D

    """

    def __init__(self, bus=1, address=0x69, name=""):
        """
        Constructor

        :param bus: int Busnumber
        :param address: int Address in the form 0x69
        :param name: str
        """
        self.l3g4200d = tmp.L3G4200D(smbus.SMBus(bus), address, name)

    def get_gyro(self):
        """
        Returns the scaled Gyro values as a dictionary with 'x', 'y' and 'z' as indices, in radians/second

        :return: dict
        """
        return {'x': self.l3g4200d.read_scaled_gyro_x(),
                'y': self.l3g4200d.read_scaled_gyro_y(),
                'z': self.l3g4200d.read_scaled_gyro_z()
                }

    def get_raw_gyro(self):
        """
        Returns the raw Gyro values as a dictionary with 'x', 'y' and 'z' as indices, in radians/second

        :return: dict
        """
        return {'x': self.l3g4200d.read_raw_gyro_x(),
                'y': self.l3g4200d.read_raw_gyro_y(),
                'z': self.l3g4200d.read_raw_gyro_z()
                }

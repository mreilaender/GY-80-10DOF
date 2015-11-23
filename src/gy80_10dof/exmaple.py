from adxl import ADXL345
from bmp import BMP085
from hmc import HMC5883L
from l3g4 import L3G4200D

sensorADXL = ADXL345()
accel = sensorADXL.get_acceleration()
print "[ADXL345]"
print "Acceleration: "
print "x: " + str(accel['x']) + sensorADXL.unit
print "y: " + str(accel['y']) + sensorADXL.unit
print "z: " + str(accel['z']) + sensorADXL.unit
print ""

sensorBMP = BMP085()
temperature = sensorBMP.get_temperature()
seaLevelPressure = sensorBMP.get_sealevel_pressure()
altitude = sensorBMP.get_altitude()
pressure = sensorBMP.get_pressure()

print "[BMP085]"
print "Temperature: " + str(temperature)
print "seaLevelPressure: " + str(seaLevelPressure)
print "Altitude: " + str(altitude)
print "Pressure: " + str(pressure)
print ""

sensorHMC = HMC5883L()
# Alternatively you can do
# comp = sensorHMC.get_x() or .get_y() or get_z()
comp = sensorHMC.get_xyz()

print "[HMC5883L]"
print "Compass: "
print "x: " + str(comp['x'])
print "y: " + str(comp['y'])
print "z: " + str(comp['z'])
print ""

sensorL3G4 = L3G4200D()
gyro = sensorL3G4.get_gyro()

print "[L3G4200D]"
print "Gyro: "
print "x: " + str(gyro['x'])
print "y: " + str(gyro['y'])
print "z: " + str(gyro['z'])
print ""
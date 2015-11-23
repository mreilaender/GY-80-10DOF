# Version must be in the form x.xx, it will be used to locate the dist-packages directory
# You can change this value if you want to use a different version, but 
# all libraries beeing copied, are using version 2.7
PYTHON_VERSION = 2.7

install:
	# HMC5883l library
	cp -R ./libs/libhmc5883l /usr/local/lib/python$(PYTHON_VERSION)/dist-packages
	
	# GPIO library for all Adafruit libraries
	python$(PYTHON_VERSION) ./libs/Adafruit_Python_GPIO/setup.py install
	rm -rf build/ dist/ Adafruit_GPIO.egg-info
	
	# BMP085 Adafruit
	python$(PYTHON_VERSION) ./libs/Adafruit_Python_BMP/setup.py install
	rm -rf Adafruit_BMP.egg-info dist build
	
	# ADXL345
	cp libs/adxl345.py /usr/local/lib/python$(PYTHON_VERSION)/dist-packages
	
	# L3G4200D
	cp libs/l3g4200d.py /usr/local/lib/python$(PYTHON_VERSION)/dist-packages

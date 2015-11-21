All rights reserved by Taur-Tech https://github.com/Taur-Tech/HMC5883L

# HMC5883L
Python library for Honeywell HMC5883L sensor

##Change Log

* 11.08.2015 - initial commit

##About the sensor:
 - 3-axis magnetometer
 - FS range +/-8gauss
 - I2C Digital Interface

##Requirements:
 - python-smbus

##Usage:

###Parameter list and acceptable values:

* 'sample_avg' _[samples] number of samples the sensor will average during measurement_
	* 1 (default)
	* 2 
	* 4 
	* 8 
* 'output_rate' _[Hz] the rate at which new measurement data is made available_
	* 0.75 
	* 1.5 
	* 3 
	* 7.5 
	* 15  (default)
	* 30
	* 75 
* 'bias_mode' _defines whether or not to apply a bias to the measurement, applies to all 3 axis_
	* 'normal' (default)
	* 'pos_bias'
	* 'neg_bias'
* 'gain' _[LSb/Gauss] gain applied to measurement values, applies to all 3 axis_
	* 1370
	* 1090 (default)
	* 820
	* 660
	* 440
	* 390
	* 330
	* 230
* 'resolution' _[mG/LSb] another way to set the gain, applies to all 3 axis_
	* 0.73
	* 0.92 (default)
	* 1.22
	* 1.52
	* 2.27
	* 2.56
	* 3.03
	* 4.35
* 'i2c_speed' _sets normal or high speed I2C_
	* 'normal' (default)
	* 'high'
* 'meas_mode' _sets type of measurement operation_
	* 'continuous'
	* 'single' (default)
	* 'idle'

###Method list

* get_parameter(parameter) _returns parameter value or None on error_
* set_parameter(parameter, value) _sets value for specified parameter, return True on success, False on error_
* get_field_x() _returns the field value for x axis in mG_
* get_field_y() _returns the field value for y axis in mG_
* get_field_z() _returns the field value for z axis in mG_
* get_field_xyz() _returns the field values for all axis in mG_


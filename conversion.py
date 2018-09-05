def kelvin_to_celsius(temp):
"""Convert a temperature from Kelvin to Celsius"""
	return temp - 273.15

def celsius_to_fahr(temp):
"""Convert a  temperature from Celsius to Fahreneit"""
	return temp * (9/5) + 32

def kelvin_to_fahr(temp):
"""Convert a temperature from  Kelvin to Fahreneit"""
	temp_c = kelvin_to_celsius(temp)
	result =  celsius_to_fahr(temp_c)
	return result

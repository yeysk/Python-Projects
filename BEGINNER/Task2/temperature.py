#......................
#.                    .
#. Temperature Modul  . 
#.                    .
#......................

def celcius_to_fahrenheit ():
    celcius = float(input("\nCelcius: "))
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

def fahrenheit_to_celcius():
    fahrenheit = float(input("\nFahrenheit: "))
    celcius = (fahrenheit - 32) * 1.8
    return celcius

def celcius_to_kelvin():
    celcius = float(input("\nCelcius: "))
    kelvin = celcius + 273.15
    return kelvin

def kelvin_to_celcius():
    kelvin = float(input("\nKelvin: "))   
    celcius = kelvin - 273.15
    return celcius

def fahrenheit_to_kelvin():
    fahrenheit = float(input("\nFahrenheit: "))
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    return kelvin
    
def kelvin_to_fahrenheit():
    kelvin = float(input("\nKelvin: "))
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    return fahrenheit
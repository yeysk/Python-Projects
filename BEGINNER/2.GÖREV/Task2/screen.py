#......................
#.                    .
#.    Screen Modul    .
#.                    .
#......................

import temperature
import length
import weight

def temperatureScreen():
        while True:
            try:
                print("\n***** TEMPERATURE OPERATIONS *****")
                print("\nPlease choose an operation below...")
                print("\n1. Celcius to Fahrenheit Converter")
                print("2. Fahrenheit to Celcius Converter")
                print("\n3. Celcius to Kelvin Converter")
                print("4. Kelvin to Celcius Converter")
                print("\n5. Fahrenheit to Kelvin Converter")
                print("6. Kelvin to Fahrenheit Converter")
                print("\n7.Go back to the main menu >")
                
                operation = int(input("\nYour operation: "))
                
                if (operation == 1):
                    print(temperature.celcius_to_fahrenheit())
                    return ""
                elif (operation == 2):
                    print(temperature.fahrenheit_to_celcius())
                    return ""
                elif (operation == 3):
                    print(temperature.celcius_to_kelvin())
                    return ""
                elif (operation == 4):
                    print(temperature.kelvin_to_celcius())
                    return ""
                elif (operation == 5):
                    print(temperature.fahrenheit_to_kelvin())
                    return ""
                elif (operation == 6):
                    print(temperature.kelvin_to_fahrenheit())
                    return ""
                elif (operation == 7):
                    print("Going back to the main menu...")
                    break
                else:
                    print("No such operation.Please try again...")
            except ValueError:
                print("Invalid input.Try again.")
        return ""
        
def lengthScreen():
        while True:
            try:
                print("\n***** LENGTH OPERATIONS *****")
                print("\nPlease choose an operation below...")
                print("\n1. Kilometer to Meter Converter")
                print("2. Meter to Kilometer Converter")
                print("\n3. Kilometer to Centimeter Converter")
                print("4. Centimeter to Kilometer Converter")
                print("\n5. Kilometer to Milimeter Converter")
                print("6. Milimeter to Kilometer Converter")
                print("\n7. Meter to Centimeter Converter")
                print("8. Centimeter to Meter Converter")
                print("\n9. Meter to Milimeter Converter")
                print("10. Milimeter to Meter Converter")
                print("\n11. Centimeter to Milimeter Converter")
                print("12. Milimeter to Centimeter Converter")
                print("\n13.Go back to the main menu >")
                
                operation = int(input("\nYour operation: "))
                
                if (operation == 1):
                    print(length.kilometer_to_meter())
                    return ""
                elif (operation == 2):
                    print(length.meter_to_kilometer())
                    return ""
                elif (operation == 3):
                    print(length.kilometer_to_centimeter())
                    return ""
                elif (operation == 4):
                    print(length.centimeter_to_kilometer())
                    return ""
                elif (operation == 5):
                    print(length.kilometer_to_milimeter())
                    return ""
                elif (operation == 6):
                    print(length.milimeter_to_kilometer())
                    return ""
                elif (operation == 7):
                    print(length.meter_to_centimeter())
                    return ""
                elif (operation == 8):
                    print(length.centimeter_to_meter())
                    return ""
                elif (operation == 9):
                    print(length.meter_to_milimeter())
                    return ""
                elif (operation == 10):
                    print(length.milimeter_to_meter())
                    return ""
                elif (operation == 11):
                    print(length.centimeter_to_milimeter())
                    return ""
                elif (operation == 12):
                    print(length.milimeter_to_centimeter())
                    return ""
                elif (operation == 13):
                    print("Going back to the main menu...")
                    break
                else:
                    print("No such operation.Please try again...")
            except ValueError:
                print("Invalid input.Try again.")
        return ""

def weightScreen():
        while True:
            try:
                print("\n***** WEIGHT OPERATIONS *****")
                print("\nPlease choose an operation below...")
                print("\n1. Ton to Kilogram Converter")
                print("2. Kilogram to Ton Converter")
                print("\n3. Ton to Gram Converter")
                print("4. Gram  to Ton Converter")
                print("\n5. Ton to Miligram Converter")
                print("6. Miligram to Ton Converter")
                print("\n7. Kilogram to Gram Converter")
                print("8. Gram to Kilogram Converter")
                print("\n9. Kilogram to Miligram Converter")
                print("10. Miligram to Kilogram Converter")
                print("\n11. Gram to Miligram Converter")
                print("12. Miligram to Gram Converter")
                print("\n13.Go back to the main menu >")
                
                operation = int(input("\nYour operation: "))
                
                if (operation == 1):
                    print(weight.ton_to_kilogram())
                    return ""
                elif (operation == 2):
                    print(weight.kilogram_to_ton())
                    return ""
                elif (operation == 3):
                    print(weight.ton_to_gram())
                    return ""
                elif (operation == 4):
                    print(weight.gram_to_ton())
                    return ""
                elif (operation == 5):
                    print(weight.ton_to_miligram())
                    return ""
                elif (operation == 6):
                    print(weight.miligram_to_ton())
                    return ""
                elif (operation == 7):
                    print(weight.kilogram_to_gram())
                    return ""
                elif (operation == 8):
                    print(weight.gram_to_kilogram())
                    return ""
                elif (operation == 9):
                    print(weight.kilogram_to_miligram())
                    return ""
                elif (operation == 10):
                    print(weight.miligram_to_kilogram())
                    return ""
                elif (operation == 11):
                    print(weight.gram_to_miligram())
                    return ""
                elif (operation == 12):
                    print(weight.miligram_to_gram())
                    return ""
                elif (operation == 13):
                    print("Going back to the main menu...")
                    break
                else:
                    print("No such operation.Please try again...")
            except ValueError:
                print("Invalid input.Try again.")
        return ""

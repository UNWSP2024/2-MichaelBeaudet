#Author: Michael Beaudet
#Title: Week 2 Program 4
#Date: 1/28/25
def temp_conversion(celsius):
    fahrenheit = 0.0
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")

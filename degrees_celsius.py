# Write a program that will convert degrees fahrenheit to degrees celsius.
Fahrenheit = int(input("Enter a Fahrenheit value to convert it to Celsius: "))

Celsius = (Fahrenheit - 32) * 5.0 / 9.0

print("The temperature :", Fahrenheit, "Fahrenheit is ", Celsius, " C")
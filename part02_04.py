Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	for i in range(5):
		celsius = eval(input("What is the Celsius temperature? "))
		fahrenheit = 9/5 * celsius + 32
		print("The temperature is", fahrenheit, "degrees Fahrenheit.")

>>> main()
What is the Celsius temperature? 0
The temperature is 32.0 degrees Fahrenheit.
What is the Celsius temperature? 25
The temperature is 77.0 degrees Fahrenheit.
What is the Celsius temperature? 50
The temperature is 122.0 degrees Fahrenheit.
What is the Celsius temperature? 75
The temperature is 167.0 degrees Fahrenheit.
What is the Celsius temperature? 100
The temperature is 212.0 degrees Fahrenheit.
>>> 

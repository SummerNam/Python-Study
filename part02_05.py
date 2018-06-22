Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	celsius = eval(input("What is the Celsius temperature? :"))
	for i in range(11):
		fahrenheit = 9/5 * celsius +32
		print(celsius, "Celsius temperature is", fahrenheit, "degrees Fahrenheit.")
		celsius = celsius + 10

>>> main()
What is the Celsius temperature? :0
0 Celsius temperature is 32.0 degrees Fahrenheit.
10 Celsius temperature is 50.0 degrees Fahrenheit.
20 Celsius temperature is 68.0 degrees Fahrenheit.
30 Celsius temperature is 86.0 degrees Fahrenheit.
40 Celsius temperature is 104.0 degrees Fahrenheit.
50 Celsius temperature is 122.0 degrees Fahrenheit.
60 Celsius temperature is 140.0 degrees Fahrenheit.
70 Celsius temperature is 158.0 degrees Fahrenheit.
80 Celsius temperature is 176.0 degrees Fahrenheit.
90 Celsius temperature is 194.0 degrees Fahrenheit.
100 Celsius temperature is 212.0 degrees Fahrenheit.
>>> 

Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Calculate the price of coffee shipments
>>> 
>>> def main():
	print("This program calculates the total price of coffee shipments.")
	pound = float(input("How many pounds of coffee do you want: "))
	
	shipprice = 1.50 + 0.86 * pound
	coffeecost = 10.5 * pound
	
	print("The price of shipping is", shipprice, "dollar.")
	print("The price of cost of coffee is", coffeecost, "dollar.")
	print("The total price is", shipprice + coffeecost, "dollar.")

>>> main()
This program calculates the total price of coffee shipments.
How many pounds of coffee do you want: 1
The price of shipping is 2.36 dollar.
The price of cost of coffee is 10.5 dollar.
The total price is 12.86 dollar.
>>> 

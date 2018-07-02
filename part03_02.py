Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # part03_02. Write a program that calculates the cost per square inch of a circular pizza, given its diameter and price.
>>> 
>>> import math
>>> 
>>> def main():
	print("This program computes the cost per square inch of a pizza")

	d = float(input("Enter the diameter of the pizza(in inches):"))
	p = int(input("Enter the price of pizza(in cents) : "))
	A = math.pi * ((d/2)**2)
	cost = p / A

	print("The cost is", cost, "cents per square inch.")

>>> main()
This program computes the cost per square inch of a pizza
Enter the diameter of the pizza(in inches):10
Enter the price of pizza(in cents) : 100
The cost is 1.2732395447351628 cents per square inch.
>>> 

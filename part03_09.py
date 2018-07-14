Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Area of triangle using Heron's formula
>>> 
>>> import math
>>> def main():
	a = float(input("Enter the length of side a: "))
	b = float(input("Enter the length of side b: "))
	c = float(input("Enter the length of side c: "))
	
	s = (a+b+c)/2
	A = math.sqrt(s*(s-a)*(s-b)*(s-c))
	
	print("This area is", A, "square units.")

>>> main()
Enter the length of side a: 3
Enter the length of side b: 4
Enter the length of side c: 5
This area is 6.0 square units.
>>> 

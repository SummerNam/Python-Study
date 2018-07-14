Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Calculates the distance between two points
>>> 
>>> import math
>>> 
>>> def main():
	x1 = float(input("Enter the x for the first point :"))
	y1 = float(input("Enter the y for the first point :"))
	
	x2 = float(input("Enter the x for the second point :"))
	y2 = float(input("Enter the y for the second point :"))
	
	d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	
	print("The distance between two points is", d)

>>> main()
Enter the x for the first point :0
Enter the y for the first point :0
Enter the x for the second point :2
Enter the y for the second point :2
The distance between two points is 2.8284271247461903
>>> 

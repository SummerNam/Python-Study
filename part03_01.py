Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #5. Write a program to calculate the volume and surface area of a sphere from its radius, given as input.

>>> import math
>>> def main():
	r = float(input("Enter radius of a sphere :"))
	V = 4 / 3 * math.pi * (r**3)
	A = 4 * math.pi * (r**2)
	print("volume of a sphere :", V, "surface area of a sphere :",A)

>>> main()
Enter radius of a sphere :1
volume of a sphere : 4.1887902047863905 surface area of a sphere : 12.566370614359172
>>> 

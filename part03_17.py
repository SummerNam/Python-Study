Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Square root using Newton's method.
>>> 
>>> import math
>>> def main():
	x = float(input("Enter number to find the root of: "))
	n = int(input("How many iterations should I use? "))

	sum = x/2.0
	for i in range(n):
		sum = (sum + x/sum)/2.0
		
	print("Approximate square root:", sum)
	print("Difference from math.sqrt:", math.sqrt(x) - sum)

>>> main()
Enter number to find the root of: 9
How many iterations should I use? 9
Approximate square root: 3.0
Difference from math.sqrt: 0.0
>>> 

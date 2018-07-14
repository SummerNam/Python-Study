Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Compute length of ladder needed.
>>> 
>>> import math
>>> def main():
	h = float(input("How high must you reach? :"))
	a = float(input("What will the ladder angle be (in degrees)? :"))
	
	radians = math.pi * a / 180
	length = h / math.sin(radians)
	
	print("Length of ladder required: ",length)

>>> main()
How high must you reach? :10
What will the ladder angle be (in degrees)? :60
Length of ladder required:  11.547005383792516
>>> 

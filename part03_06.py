Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Determine slope of a line through two points
>>> 
>>> def main():
	x1 = int(input("Enter the x for the first point :"))
	y1 = int(input("Enter the y for the first point :"))
	
	x2 = int(input("Enter the x for the second point :"))
	y2 = int(input("Enter the y for the second point :"))
	
	slope = (y2 - y1) / (x2 - x1)
	
	print("The slope of the line is", slope)

>>> main()
Enter the x for the first point :0
Enter the y for the first point :0
Enter the x for the second point :2
Enter the y for the second point :2
The slope of the line is 1.0
>>> 

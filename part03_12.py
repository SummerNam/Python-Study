Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n = int(input("Enter a number :"))
	
	sum=0
	for i in range(1,n+1):
		sum = sum + i**3
	print("The sum of cubes of 1 though number", n, "is", sum)

>>> main()
Enter a number :3
The sum of cubes of 1 though number 3 is 36
>>> 

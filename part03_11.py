Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n = int(input("Enter a number :"))
	
	sum=0
	for i in range(1,n+1):
		sum = sum+i
		
	print("The sum from 1 to", n, "is", sum)

>>> main()
Enter a number :10
The sum from 1 to 10 is 55
>>> 

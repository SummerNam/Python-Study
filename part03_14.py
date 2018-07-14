Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Average of numbers entered by the user.
>>> 
>>> def main():
	n = int(input("How many numbers do you have: "))
	sum=0
	
	for i in range(n):
		num = float(input("Enter a number: "))
		sum = sum + num
		
	print("The average of the numbers is", sum/n)

>>> main()
How many numbers do you have: 3
Enter a number: 3
Enter a number: 4
Enter a number: 5
The average of the numbers is 4.0
>>> 

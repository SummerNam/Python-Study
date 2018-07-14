Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	n = int(input("How many numbers do you have? :"))
	sum=0
	
	for i in range(n):
		num = int(input("Enter a number: "))
		sum = sum + num
		
	print("The sum of the numbers is:", sum)

>>> main()
How many numbers do you have? :3
Enter a number: 1
Enter a number: 3
Enter a number: 5
The sum of the numbers is: 9
>>> 

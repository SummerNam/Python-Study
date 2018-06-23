Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program calculates the future value.")

	principal = eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the annual interest rate: "))
	y = eval(input("Enter the number of years: "))
	
	for i in range(y):
		principal = principal * (1 + apr)
		
	print("The value in", y, "years is: ", principal)

>>> main()
This program calculates the future value.
Enter the initial principal: 10000
Enter the annual interest rate: 0.2
Enter the number of years: 10
The value in 10 years is:  61917.36422399999
>>> 

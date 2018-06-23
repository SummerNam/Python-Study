Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program calculates the future value of a yearly investment.")

	payment = eval(input("Enter amount to invest each year: "))
	principal = 0
	apr = eval(input("Enter the annual interest rate: "))
	y = eval(input("Enter the number of years: "))
	
	for i in range(y):
		principal = (principal+payment) * (1 + apr)
		
	print("The value in", y, "years is: ", principal)

>>> main()
This program calculates the future value of a yearly investment.
Enter amount to invest each year: 10000
Enter the annual interest rate: 0.1
Enter the number of years: 10
The value in 10 years is:  175311.67061100013
>>> 

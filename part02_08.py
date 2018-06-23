Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
    print("This program calculates the future value")
    
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding perios per year: "))

    for i in range(10 * periods):
        principal = principal * (1+rate/periods)

    print("The amount in 10 years is:", principal)

>>> main()
This program calculates the future value
Enter the initial principal: 10000
Enter the interest rate: 0.01
Enter the number of compounding perios per year: 2
The amount in 10 years is: 11048.955771867288
>>> 

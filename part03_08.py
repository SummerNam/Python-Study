Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
    print("This program calculates the Gregorian epact value of year.")
    
    year = int(input("Enter the year :"))
    c= year//100
    
    epact = (8+(c//4)-c + ((8*c+13)//25) + 11 * (year%19)) % 30
    
    print("The epact value is", epact, "days.")

>>> main()
This program calculates the Gregorian epact value of year.
Enter the year :2018
The epact value is 13 days.
>>> 

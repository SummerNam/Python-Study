Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #part03_03. Write a program that determines the molecular weight of a hydrocarbon based on the number of hydrogen, carbon, and oxygen atoms. You should use the following weight
>>> 
>>> def main():
	h= int(input("Enter the number of hydrogen atoms: "))
	c= int(input("Enter the number of carbon atoms: "))
	o= int(input("Enter the number of oxygen atoms: "))
	weight = 1.00794 * h + 12.0107 * c + 15.9994 * o
	
	print("The molecular of a hydrocarbon is: ", weight)

>>> main()
Enter the number of hydrogen atoms: 2
Enter the number of carbon atoms: 1
Enter the number of oxygen atoms: 1
The molecular of a hydrocarbon is:  30.025979999999997
>>> 

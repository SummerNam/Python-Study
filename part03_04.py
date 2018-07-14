Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Write a program that determines the distance to a lighting strike based on the time elapsed between the flash and the sound of thunder.
>>> 
>>> def main():
	print("This program calculates the distance from a lighting strike.")
	
	seconds = int(input("Enter number of seconds between flash and crash: "))
	m= 340 * seconds
	
	print("The lighting is approximately", m, "m away.")

>>> main()
This program calculates the distance from a lighting strike.
Enter number of seconds between flash and crash: 10
The lighting is approximately 3400 m away.
>>> 

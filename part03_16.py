Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Nth fibonacci number
>>> 
>>> def main():
	n = int(input("Enter the value of n: "))
	fst, snd = 1,1
	for i in range(n-2):
		fst, snd = fst+snd ,fst
		
	print("The nth Fibonacci number is", fst)

>>> main()
Enter the value of n: 6
The nth Fibonacci number is 8
>>> 

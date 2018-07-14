Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Approximation of pi using Taylor series.
>>> 
>>> import math
>>> 
>>> def main():
	n = int(input("How many terms should I use? :"))
	
	sum=0.0
	alter=1.0
	
	for i in range(1, 2*n, 2):
		num = 4.0 / i
		sum = sum + alter * num
		alter = -alter
		
	print("Approximation to pi is:", sum)
	print("Difference from math.pi:", math.pi - sum)

>>> main()
How many terms should I use? :3
Approximation to pi is: 3.466666666666667
Difference from math.pi: -0.32507401307687367
>>> 

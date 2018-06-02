Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print('assignment 05 of part 01')
	x = eval(input('Enter a number between 0 and 1'))
	n = eval(input('How many numbers should I print?'))
	for i in range(n):
		x = 3.9 * x * (1 - x)
		print(x)

>>> main()
assignment 05 of part 01
Enter a number between 0 and 1.25
How many numbers should I print?15
0.73125
0.76644140625
0.6981350104385375
0.8218958187902304
0.5708940191969317
0.9553987483642099
0.166186721954413
0.5404179120617926
0.9686289302998042
0.11850901017563877
0.4074120362630336
0.9415671289870646
0.214572035332672
0.6572704202448796
0.8785374581723959
>>> 

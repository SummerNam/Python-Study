Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print('assignment 03 of part 01')
	x=eval(input('Enter a number between 0 and 1 :'))
	for i in range(10):
		x=2.0 * x * (1 - x)
		print(x)

>>> main()
assignment 03 of part 01
Enter a number between 0 and 1 :0.25
0.375
0.46875
0.498046875
0.49999237060546875
0.4999999998835847
0.5
0.5
0.5
0.5
0.5
>>> main()
assignment 03 of part 01
Enter a number between 0 and 1 :0.26
0.38480000000000003
0.47345792000000003
0.49859103597854726
0.4999960296407725
0.4999999999684725
0.49999999999999994
0.49999999999999994
0.49999999999999994
0.49999999999999994
0.49999999999999994
>>> 

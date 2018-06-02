Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # chaos.py
>>> # 혼돈 함수의 간단한 예를 보여 주는 프로그램
>>> 
>>> def main():
	print("This program illustrates a chaotic function.")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10) :
		x = 3.9 * x * (1-x)
		print(x)

>>> main()
This program illustrates a chaotic function.
Enter a number between 0 and 1: 0.25
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
>>> 
>>> main()
This program illustrates a chaotic function.
Enter a number between 0 and 1: 0.26
0.75036
0.73054749456
0.7677066257332165
0.6954993339002887
0.8259420407337192
0.5606709657211202
0.9606442322820199
0.14744687593470315
0.49025454937601765
0.9746296021493285
>>> 

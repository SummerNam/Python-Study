Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	for i in range(100):
		answer = eval(input("please enter formula ex)1+2 "))
		print("The answer is", answer)

>>> main()
please enter formula ex)1+2 3+4
The answer is 7
please enter formula ex)1+2 5-6
The answer is -1
please enter formula ex)1+2 7*8
The answer is 56
please enter formula ex)1+2 9/10
The answer is 0.9
please enter formula ex)1+2 11/0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    main()
  File "<pyshell#1>", line 3, in main
    answer = eval(input("please enter formula ex)1+2 "))
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 

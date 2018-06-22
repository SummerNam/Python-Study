Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
	print("This program computes the average of three exam scores")
	score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
	average = (score1 + score2+ score3)/3
	print("The average of the scores is:", average)

>>> main()
This program computes the average of three exam scores
Enter three scores separated by a comma: 90,80,70
The average of the scores is: 80.0
>>> 

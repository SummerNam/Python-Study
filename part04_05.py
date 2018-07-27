Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> 
>>> def main():
	win = GraphWin()
	
	b1 = Rectangle(Point(0,0),Point(20,20))
	b1.setOutline('black')
	
	b2 = Rectangle(Point(20,20),Point(40,40))
	b2.setOutline('black')

	b3 = Rectangle(Point(40,40),Point(60,60))
	b3.setOutline('black')

	b4 = Rectangle(Point(60,60),Point(80,80))
	b4.setOutline('black')

	b5 = Rectangle(Point(80,80),Point(100,100))
	b5.setOutline('black')
	
	b1.draw(win)
	b2.draw(win)
	b3.draw(win)
	b4.draw(win)
	b5.draw(win)
	
	t1 = Text(Point(10,10), '1')
	t2 = Text(Point(30,30), '2')
	t3 = Text(Point(50,50), '3')
	t4 = Text(Point(70,70), '4')
	t5 = Text(Point(90,90), '5')
	
	t1.draw(win)
	t2.draw(win)
	t3.draw(win)
	t4.draw(win)
	t5.draw(win)

>>> main()
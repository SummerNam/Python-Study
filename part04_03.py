Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> 
>>> def main():
	win = GraphWin()
	c1 = Circle(Point(100,100),50)
	c1.setFill('yellow')
	
	c2 = Circle(Point(110,85),10)
	c2.setFill('black')
	
	c3 = Circle(Point(80,85),10)
	c3.setFill('black')
	
	c4 = Oval(Point(120,130), Point(70,110))
	c4.setFill('orange')

	c1.draw(win)
	c2.draw(win)
	c3.draw(win)
	c4.draw(win)
	
	win.getMouse()
	win.close()

>>> main()
>>> 

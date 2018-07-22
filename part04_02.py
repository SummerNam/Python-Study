Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> 
>>> def main():
	win = GraphWin()
	win.setCoords(-6,-6,6,6)
	#좌하단(-6,-6), 우상단(6,6)
	win.setBackground('gray')
	center = Point(0,0)
	
	c1 = Circle(center,5)
	c1.setFill('white')
	c1.draw(win)

	c2 = Circle(center,4)
	c2.setFill('black')
	c2.draw(win)

	c3 = Circle(center,3)
	c3.setFill('blue')
	c3.draw(win)

	c4 = Circle(center,2)
	c4.setFill('red')
	c4.draw(win)

	c5 = Circle(center,1)
	c5.setFill('yellow')
	c5.draw(win)

	win.getMouse()
	win.close()

>>> main()
>>> 

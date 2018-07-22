Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> 
>>> def main():
	win = GraphWin()
	shape = Rectangle(Point(1,1),Point(20,20))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()
		dx = p.getX() - c.getX()
		dy = p.getY() - c.getY()
		shape = shape.clone()
		shape.move(dx,dy)
		shape.draw(win)
	Text(Point(100,180), 'Click again to quit.').draw(win)
	win.getMouse()
	win.close()

>>> main()
>>> 

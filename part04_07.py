Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> import math
>>> 
>>> def main():
	radius = float(input("Enter the radius of the circle: "))
	yinter = float(input("Enter the y-intercept of the line: "))
	
	win = GraphWin()
	win.setCoords(-10,-10,10,10)
	
	Circle(Point(0,0),radius).draw(win)
	Line(Point(-10,yinter), Point(10,yinter)).draw(win)
	
	x = math. sqrt(radius * radius - yinter * yinter)
	print("X values of intersection", -x, x)
	
	p1 = Circle(Point(x,yinter),0.25)
	p1.setOutline("red")
	p1.setFill("red")
	p1.draw(win)
	
	p2 = p1.clone()
	p2.move(-2*x, 0)
	p2.draw(win)
	
	win.getMouse()
	win.close()

>>> main()
Enter the radius of the circle: 5
Enter the y-intercept of the line: 2
X values of intersection -4.58257569495584 4.58257569495584

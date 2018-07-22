Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> 
>>> def main():
    win=GraphWin("Winter Scene",500,500)
    win.setCoords(0,0,200,200)
    win.setBackground("blue")

    # Body of the snowman
    c1 = Circle(Point(50,40),40)
    c1.draw(win)
    c1.setFill("white")
    c1.setOutline("white")

    c2 = Circle(Point(50,100),30)
    c2.draw(win)
    c2.setFill("white")
    c2.setOutline("white")

    c3 = Circle(Point(50,145),20)
    c3.draw(win)
    c3.setFill("white")
    c3.setOutline("white")

    # Top Hat of Snowman
    r1 = Rectangle(Point(30,160),Point(70,165))
    r1.draw(win)
    r1.setFill("black")

    r2 = Rectangle(Point(40,165),Point(60,185))
    r2.draw(win)
    r2.setFill("black")

    # Eyes of the Snowman
    e1 = Circle(Point(42.5,150),2.5)
    e1.draw(win)
    e1.setFill("black")

    e2 = Circle(Point(57.5,150),2.5)
    e2.draw(win)
    e2.setFill("black")

    # Nose of the Snowman
    n = Polygon(Point(50,142.5),Point(50,137.5),Point(57.5,140))
    n.draw(win)
    n.setOutline("orange")
    n.setFill("orange")

    # Mouth of the Snowman
    m1 = Circle(Point(40,135),1)
    m1.draw(win)
    m1.setFill("black")

    m2 = Circle(Point(45,130),1)
    m2.draw(win)
    m2.setFill("black")

    m3 = Circle(Point(50,127.5),1)
    m3.draw(win)
    m3.setFill("black")

    m4 = Circle(Point(55,130),1)
    m4.draw(win)
    m4.setFill("black")

    m5 = Circle(Point(60,135),1)
    m5.draw(win)
    m5.setFill("black")

    # Buttons on the Snowman
    b1 = Circle(Point(50,115),3)
    b1.draw(win)
    b1.setFill("black")

    b2 = Circle(Point(50,105),3)
    b2.draw(win)
    b2.setFill("black")

    b3 = Circle(Point(50,95),3)
    b3.draw(win)
    b3.setFill("black")

    # Christmas Tree
    rect1 = Rectangle(Point(140,0),Point(160,25))
    rect1.draw(win)
    rect1.setOutline("brown")
    rect1.setFill("brown")
    
    t1 = Polygon(Point(100,25),Point(200,25),Point(150,65))
    t1.draw(win)
    t1.setOutline("forest green")
    t1.setFill("forest green")

    t2 = Polygon(Point(110,60),Point(190,60),Point(150,100))
    t2.draw(win)
    t2.setOutline("forest green")
    t2.setFill("forest green")

    t3 = Polygon(Point(120,90),Point(180,90),Point(150,120))
    t3.draw(win)
    t3.setOutline("forest green")
    t3.setFill("forest green")

    t4 = Polygon(Point(130,115),Point(170,115),Point(150,135))
    t4.draw(win)
    t4.setOutline("forest green")
    t4.setFill("forest green")

    t5 = Polygon(Point(135,132.5),Point(165,132.5),Point(150,155))
    t5.draw(win)
    t5.setOutline("forest green")
    t5.setFill("forest green")

    # Star on the Christmas Tree
    n = Polygon(Point(150,152.5),Point(147.5,160),Point(140,162.5),Point(147.5,165),Point(150,172.5),Point(152.5,165),Point(160,162.5),Point(152.5,160))
    n.draw(win)
    n.setOutline("gold")
    n.setFill("gold")

>>> main()
>>> 

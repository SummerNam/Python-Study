Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> 
>>> def main():
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    # Set coordinates for easy display of prompts.
    win.setCoords(0,0,10,10)

    # Display prompts
    t1 = Text(Point(5,8), "Plotting a 10 year investment")
    t1.setSize(14)
    t1.draw(win)

    t2 = Text(Point(5,7.5), "Enter the information below and then click anywhere")
    t2.setSize(14)
    t2.draw(win)

    t3 = Text(Point(2,6), "Initial Principal:")
    t3.setSize(14)
    t3.draw(win)

    prinBox = Entry(Point(4.5,6), 6)
    prinBox.draw(win)
    prinBox.setText("2000")

    t4 = Text(Point(2,4), "Annual Interest Rate:")
    t4.setSize(14)
    t4.draw(win)

    aprBox = Entry(Point(4.5,4), 6)
    aprBox.setText("0.05")
    aprBox.draw(win)

    # wait for mouse click and get values
    win.getMouse()
    principal = float(prinBox.getText())
    apr = float(aprBox.getText())

    # Erase the prompts
    t1.undraw()
    t2.undraw()
    t3.undraw()
    t4.undraw()
    prinBox.undraw()
    aprBox.undraw()


    # Set Window coords for drawing the graph.
    win.setCoords(-1.75,-200, 11.5, 10400)

    # Create a graphics window with labels on left edge
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

>>> main()
>>> 

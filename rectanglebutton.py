# rectanglebutton.py
# A Python module to create rectangle buttons
# Created by Andy Exley, adopted by Frederik Roenn Stensaeth and Javier Moran
# 03.17.15
# Disclaimer: We have not commented the code that Andy Exley wrote

# Import graphics library
from graphics import *


#creates a rectangle ship, that creates the sea spaces, and wether or not
#they have a ship. Contains draw, undraw, clicked, deactivate, activate,
#hit, outline, and get_center methods.
class RectangleButton:


    def __init__(self, center, width, height, color, ship):
        
        w, h = width / 2.0, height / 2.0
        self.xmin, self.xmax = center.getX() - w, center.getX() + w
        self.ymin, self.ymax = center.getY() - h, center.getY() + h
        self.rect = Rectangle(Point(self.xmin, self.ymin), 
                                Point(self.xmax, self.ymax))
        self.center = center
        self.sea_space_ship = ship
        self.rect.setFill(color)
        self.activate()

    def draw(self, window):
        
        self.rect.draw(window)


    def undraw(self):
        
        self.rect.undraw()


    def clicked(self, p):
        
        if (self.active and self.xmin <= p.getX() <= self.xmax and 
                self.ymin <= p.getY() <= self.ymax):
            return True


	#deactivates a sea space if it was shot, sets it to dark blue
	#if there was no ship in it. Takes self as parameter
    def deactivate(self):
        
        self.rect.setWidth(2)
        # Fill rectangle darkblue
        self.rect.setFill('darkblue')
        # Set self.active to False
        self.active = False


    # Define activate method. Takes self as parameter.
    def activate(self):
        
        self.rect.setWidth(2)
        # Set self.active to True
        self.active = True


	#deactivates a sea space
	#turns it red if there was a ship in it, indicating a hit.
	# Takes self as parameter
    def hit(self):
        
        # If self.active is True, deactivate button and fill red
        if self.active:
            self.rect.setWidth(2)
            self.deactivate()
            self.rect.setFill('red')
        # Set self.active to False
        self.active = False


    # Define outline method. Takes self and color as parameters. Sets outlne
    #of button to color
    def outline(self, color):
        
        self.rect.setOutline(color)


    # Define get_center method. Takes self as paramater. Returns center
    def get_center(self):
        
        return self.center


	#returns wethere or not the sea space had a ship or not
	#in the form of True or False
    def get_ship_status(self):
        
        return self.sea_space_ship
        
        
	#tells a button that a ship is being placed on top of it
    def update_ship(self):
        
        self.sea_space_ship = True


    def active_button(self):
        
        return self.active

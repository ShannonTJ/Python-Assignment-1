#This program draws a face and centers it based on coordinates that the user inputs
#Shannon TJ 10101385

#Prompt the user to enter an x and y coordinate
x = float(input("Enter an x coordinate:"))
y = float(input("Enter a y coordinate:"))

from SimpleGraphics import *

#Fill the background
background("red2")

#Draw the face
setFill("black")
ellipse(x-180,y-180, 360,360)

setFill("snow3")
ellipse(x-175,y-175, 350,350)

#Draw the mouth
setFill("black")
pieSlice(x-55,y+97, 110,85, 0,180)

setFill("azure")
pieSlice(x-50,y+100, 100,75,  0,180)

#Draw the eyes
setOutline("snow4")
setFill("snow4")
ellipse(x-140,y+10, 100,75)
ellipse(x+40,y+10, 100,75)

setFill("black")
ellipse(x-145,y-5, 110,85)
ellipse(x+35,y-5, 110,85)

setOutline("black")
setFill("orange")
ellipse(x-140,y, 100,75)
ellipse(x+40,y, 100,75)

setFill("black")
ellipse(x-115,y, 50,60)
ellipse(x+65,y, 50,60)

#Draw the eyebrows
setFill("black")
polygon(x-125,y-25, x-25,y+10, x-25,y+20, x-125,y-25)
polygon(x+125,y-25, x+25,y+10, x+25,y+20, x+125,y-25)

#Draw the hair
setFill("black")
polygon(x-25,y-75, x+25,y-75, x,y, x-25,y-75)
polygon(x-25,y-75, x-50,y+25, x-75,y-75, x-25,y-75)
polygon(x+25,y-75, x+50,y+25, x+75,y-75, x+25,y-75)
polygon(x-75,y-75, x-125,y+50, x-175,y-75, x-75,y-75)
polygon(x+75,y-75, x+125,y+50, x+175,y-75, x+75,y-75)

polygon(x+155,y+75, x+225,y-85, x+155,y-85, x+155,y+75)
polygon(x-155,y+75, x-225,y-85, x-155,y-85, x-155,y+75)

polygon(x-225,y-150, x-175,y-150, x-175,y-75, x-225,y-150)
polygon(x-175,y-150, x,y-240, x-50,y-75, x-175,y-75, x-175,y-150)

polygon(x-125,y-75, x-175,y-110, x+75,y-240, x+55,y-75, x-125,y-75)
polygon(x-25,y-75, x-75,y-110, x+175,y-240, x+155,y-75, x-25,y-75)
polygon(x+100,y-75, x+50,y-150, x+225,y-150, x+175,y-75, x+100,y-75)

#Draw the horns
setOutline("orange red")
setFill("orange red")
blob(x-140,y-100, x-100,y-150, x-60,y-100, x-140,y-100)
blob(x+140,y-100, x+100,y-150, x+60,y-100, x+140,y-100)

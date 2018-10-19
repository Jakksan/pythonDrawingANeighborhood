from turtle import *
import math
import time

#setup(1000,1000)
goto(0,0)
penup()

###########################################
# drawTriangle()
#       Draw a triangle depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# tri_base : int
#     the length of the triangle base
# tri_height : int
#     the height of the triangle
# color : str
#     the color of the triangle
#
# Returns
# -------
# none
###########################################

def drawTriangle(x, y, tri_base, tri_height, color):
    # Calculate all the measurements and angles needed to draw the triangle
    side_length = math.sqrt((0.5*tri_base)**2 + tri_height**2)
    base_angle = math.degrees(math.atan(tri_height/(tri_base/2)))
    top_angle = 180 - (2 * base_angle)

    # Draw the triangle using the calculations from above
    penup()
    goto(x, y)
    pendown()
    setheading(0)

    fillcolor(color)
    begin_fill()

    forward(tri_base)
    left(180 - base_angle)
    forward(side_length)
    left(180 - top_angle)
    forward(side_length)

    end_fill()
    penup()

# drawTriangle(0, 0, 250, 40)

###########################################
# drawRectangle()
#       Draw a rectangle depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# rec_width : int
#     the length of the rectangle base
# rect_height : int
#     the height of the rectangle
# color : str
#     color of the rectangle
#
# Returns
# -------
# none
###########################################

def drawRectangle(x, y, rec_width, rect_height, color):

    penup()
    goto(x, y)

    pendown()
    setheading(0)

    fillcolor(color)
    begin_fill()

    for each in range(2):
        forward(rec_width)
        left(90)
        forward(rect_height)
        left(90)

    end_fill()

    penup()

# drawRectangle(0, 0, 50, 55)

###########################################
# drawCircle()
#       Draw a circle depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# radius : int
#     radius of the circle
# color : str
#     color of the circle
#
# Returns
# -------
# none
###########################################

def drawCircle(x, y, radius, color):

    penup()

    setheading(0)
    setpos(x, (y-radius))

    pendown()

    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

    penup()

# drawCircle(0, 0, 90)

###########################################
# drawTree()
#       Draw a tree depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# tree_height : int
#     height of the tree
# color : str
#     color of the canopy of the tree
#
# Returns
# -------
# none
###########################################

def drawTree(x, y, tree_height, color):


    drawRectangle((x-(tree_height * 0.1)), y, (tree_height * 0.2), tree_height * 0.5, "sandy brown")

    drawCircle(x, (y + (tree_height * 0.75)), (tree_height * 0.25), color)

# drawTree(200, 20, 120)

###########################################
# drawHouse()
#       Draw a house depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# house_width : int
#     width of the hosue
# house_height : int
#     height of the house
# primary_color : str
#     color of the building
# secondary_color : str
#     color of the roof
#
# Returns
# -------
# none
###########################################

def drawHouse(x, y, house_width, house_height, primary_color, secondary_color):

    # Define some variables that will be useful for house construction
    roof_height = house_height * 0.2
    building_height = house_height * 0.8

    # Draw building
    drawRectangle(x, y, house_width, building_height, primary_color)

    # create variables needed for drawing the door
    door_width = house_width / 8
    door_height = house_height / 4

    # Draw door
    door_x = x+(house_width * 0.75)
    door_y = y
    drawRectangle(door_x, door_y, door_width, door_height, "brown")
    drawCircle(door_x + door_width*3/4, door_y + door_height/2, 3, "gold")

    # Draw roof
    overhang = 20
    drawTriangle(x-(overhang / 2), (y + building_height), (house_width + overhang), roof_height, secondary_color)

    # Draw window
    window_size = building_height / 2
    window_x = (x+(house_width * 0.2))
    window_y = y + (building_height / 3)
    drawRectangle(window_x, window_y, window_size, window_size/2, "light blue")

    # Draw the window sections
    goto(window_x + window_size/2, window_y)
    pendown()
    goto(window_x + window_size/2, window_y + window_size/2)
    penup()
    goto(window_x, window_y + window_size/4)
    pendown()
    goto(window_x + window_size, window_y + window_size/4)

    penup()

###########################################
# drawTownSign
#       Draw a sign with the town name depending on parameters
#
# Parameters
# ----------
# x : int
#     x coordinate of the anchorpoint
# y : int
#     y coordinate of the anchorpoint
# text : str
#     text to be printed on the sign
#
# Returns
# -------
# none
###########################################

def drawTownSign(x, y, text):

    letters = len(list(text))
    sign_width = (letters*10)+10

    # Draw the rectangular feet of the sign
    drawRectangle((x+sign_width/2-5), y, 10, 75, "brown")
    drawRectangle((x-sign_width/2-5), y, 10, 75, "brown")


    if letters < 10:
        sign_width = 120

    drawRectangle(x-(0.5*sign_width), y+15, sign_width, 60, "light grey")

    setpos(x, y+50)
    write("Welcome to", align="center", font=("Monaco", 12, "normal"))
    setpos(x, y+20)
    write(text, align="center", font=("Monaco", 12, "normal"))



################################################################################
# Start Drawing the Neighborhood


# Read each file
infile = open("input_file.txt")
text_array = []

# read the first line
line = infile.readline()

# Do this loop until we reach the end of the file
while line:

    # remove newline
    line = line.rstrip('\n')


    # append the line to the text array
    text_array.append(line)

    # read the next line
    line = infile.readline()

drawTownSign(0, -300, text_array[0])

for text in text_array:
    print(text + "\n")
    text = text.split()

    for i in range(len(text)):
        if "_" in text[i]:
            text[i] = text[i].replace("_", " ")

    if text[0] == "house":
        drawHouse(int(text[1]), int(text[2]), int(text[3]), int(text[4]), text[5], text[6])
    elif text[0] == "tree":
        drawTree(int(text[1]), int(text[2]), int(text[3]), text[4])
    else:
        print("ERROR, CANNOT DRAW: " + '"'+ text[0] +'"')


input()

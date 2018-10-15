from turtle import *
import math
import time

setup(1000,1000)
goto(0,0)
penup()

def drawTriangle(x, y, tri_base, tri_height):

    # Calculate all the measurements and angles needed to draw the triangle
    side_length = math.sqrt((0.5*tri_base)**2 + tri_height**2)
    base_angle = math.degrees(math.atan(tri_height/(tri_base/2)))
    top_angle = 180 - (2 * base_angle)

    # Draw the triangle using the calculations from above
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    forward(tri_base)
    left(180 - base_angle)
    forward(side_length)
    left(180 - top_angle)
    forward(side_length)
    penup()

# drawTriangle(0, 0, 250, 40)

def drawRectangle(x, y, rec_width, rect_height):
    penup()
    goto(x, y)

    pendown()
    setheading(0)

    for each in range(2):
        forward(rec_width)
        left(90)
        forward(rect_height)
        left(90)

    penup()

# drawRectangle(0, 0, 50, 55)

def drawCircle(x, y, radius):
    penup()
    setheading(0)
    setpos(x, (y-radius))
    pendown()
    circle(radius)
    penup()

# drawCircle(0, 0, 90)

def drawTree(x, y, tree_height):

    drawRectangle((x-(tree_height * 0.1)), y, (tree_height * 0.2), tree_height * 0.5)
    drawCircle(x, (y + (tree_height * 0.75)), (tree_height * 0.25))

# drawTree(200, 20, 120)

def drawHouse(x, y, house_width, house_height):

    # Define some variables that will be useful for house construction
    roof_height = house_height * 0.2
    building_height = house_height * 0.8

    # Draw building
    drawRectangle(x, y, house_width, building_height)

    # create variables needed for drawing the door
    door_width = house_width / 8
    door_height = house_height / 4

    # Draw door
    door_x = x+(house_width * 0.75)
    door_y = y
    drawRectangle(door_x, door_y, door_width, door_height)
    drawCircle(door_x + door_width*3/4, door_y + door_height/2, 3)

    # Draw roof
    overhang = 20
    drawTriangle(x-(overhang / 2), (y + building_height), (house_width + overhang), roof_height)

    # Draw window
    window_size = building_height / 2
    window_x = (x+(house_width * 0.2))
    window_y = y + (building_height / 3)
    drawRectangle(window_x, window_y, window_size, window_size/2)

    # Draw the window sections
    goto(window_x + window_size/2, window_y)
    pendown()
    goto(window_x + window_size/2, window_y + window_size/2)
    penup()
    goto(window_x, window_y + window_size/4)
    pendown()
    goto(window_x + window_size, window_y + window_size/4)

    penup()

# drawHouse(-100, -40, 300, 300)



input()

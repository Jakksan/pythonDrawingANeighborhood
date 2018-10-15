from turtle import *
import math
import time

goto(0,0)
penup()

def drawTriangle(x, y, tri_base, tri_height):

    side_length = math.sqrt((0.5*tri_base)**2 + tri_height**2)

    base_angle = math.degrees(math.atan(tri_height/(tri_base/2)))

    top_angle = 180 - (2 * base_angle)


    pendown()
    setheading(0)
    forward(tri_base)
    left(180 - base_angle)
    forward(side_length)
    left(180 - top_angle)
    forward(side_length)
    penup()

#drawTriangle(0, 0, 250, 40)

def drawRectangle(x, y, rec_width, rect_height):

    pendown()
    setheading(0)

    for each in range(2):
        forward(rec_width)
        left(90)
        forward(rect_height)
        left(90)

#drawRectangle(0, 0, 50, 55)

def drawCircle(x, y, radius):

    setheading(0)
    setpos(x, (y-radius))
    pendown()
    circle(radius)
    penup()

#drawCircle(0, 0, 90)

def drawTree(x, y, tree_height):

    drawRectangle((x-(tree_height * 0.1)), y, (tree_height * 0.2), tree_height * 0.5)
    drawCircle(x, (y + (tree_height * 0.75)), (tree_height * 0.25))

def drawHouse(x, y, house_width, house_height):
    door_width = house_width/8
    door_height = house_height/4
    drawRectangle(x, y, house_width, house_height*0.8)
    goto((x+(house_width*0.75)), y)
    drawRectangle(x, y, door_width, door_height)
    goto(x+(house_width/2), (y+house_height))
    drawTriangle(xcor(), ycor(), house_width+10, house_height*0.2)

drawHouse(0, 0, 300, 100)
# drawTree(0, 0, 60)

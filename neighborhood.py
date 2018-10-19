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


def drawPumpkin(x, y, radius):
    drawRectangle(x, y+radius-3, radius/4, radius/2)
    begin_fill()
    fillcolor("white")
    drawCircle(x, y, radius)
    end_fill()


def drawTownSign(x, y, text):
    letters = len(list(text))
    sign_width = (letters*10)+10

    drawRectangle((x-5), y, 10, 15)

    if letters < 10:
        sign_width = 120

    drawRectangle(x-(0.5*sign_width), y+15, sign_width, 60)

    setpos(x, y+50)
    write("Welcome to", align="center", font=("Monaco", 12, "normal"))
    setpos(x, y+20)
    write(text, align="center", font=("Monaco", 12, "normal"))


# drawPumpkin(0, 0, 30)
# drawHouse(-200, -200, 200, 300)


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


# print(text_array)

for text in text_array:
    print(text + "\n")
    text = text.split()

    print(text[3])

    if text[0] == "house":
        drawHouse(int(text[1]), int(text[2]), int(text[3]), int(text[4]))
    elif text[0] == "tree":
        drawTree(int(text[1]), int(text[2]), int(text[3]))

    else:
        print("other")


input()

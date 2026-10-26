import turtle
import numpy as np

t = turtle.Pen()
screen = turtle.Screen()
screen.colormode(255)
width = screen.window_width()
height = screen.window_height()

def draw_polygon(t, x, y, sides, color, size, rotation):
    t.penup()
    for i in range(sides+1):
        rot = np.deg2rad(360/sides)
        t.color(color)
        t.goto(np.cos(rot*i+rotation)*size + x, np.sin(rot*i+rotation)*size + y)
        t.pendown()
    t.penup()

def get_mouse(event):
    global x
    global y
    global width
    global height
    x = event.x - width/2
    y = -event.y + height/2
    print(x, y)

def main():
    global x
    global y
    global positions
    global num
    canvas = turtle.getcanvas()
    canvas.bind("<Motion>", get_mouse)
    for i in range(num):
        size = (i+1)*(300/num)
        positions[i][0] = positions[i][0] + (x - positions[i][0]) / size
        positions[i][1] = positions[i][1] + (y - positions[i][1]) / size
        positions[i][2] = positions[i][2] + np.deg2rad(size/1000)
        draw_polygon(t, positions[i][0], positions[i][1], 3, [int(0*(300-size)/300),int(255*(300-size)/300),int(0*(300-size)/300)], size, positions[i][2])

x = 0
y = 0
positions = []
num = 100
for i in range(num):
    positions.append([x,y, 0])

t.speed(0)
turtle.tracer(0)

while True:
    t.clear()
    main()
    screen.update()
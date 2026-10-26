import turtle
WIDTH = 980
HEIGHT = 630

def draw_line(t, x1, y1, x2, y2):
    #Draw one straight line from (x1, y1) to (x2, y2).
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def draw_point(t, x, y, color):
    t.penup()
    t.color(color)
    t.goto(x, y)
    t.dot(10)
    t.pensize(2)
    t.color("black")

def main():
    screen = turtle.Screen()
    screen.setup(1000, 660)
    screen.setworldcoordinates(0, 660, 1000, 0) # (0, 0) = top-left
    screen.tracer(0) # draw instantly
    t = turtle.Turtle()
    t.hideturtle()
    # Draw the rectangle
    draw_line(t, 10, 10, 10 + WIDTH, 10)
    draw_line(t, 10 + WIDTH, 10, 10 + WIDTH, 10 + HEIGHT)
    draw_line(t, 10 + WIDTH, 10 + HEIGHT, 10, 10 + HEIGHT)
    draw_line(t, 10, 10 + HEIGHT, 10, 10)

    num=50
    for i in range(num):
        draw_line(t, 10+((WIDTH/num)*i), 10 + HEIGHT, 10 + WIDTH, 10 + HEIGHT - (HEIGHT/num)*i)
        draw_line(t, 10 + WIDTH - ((WIDTH / num) * i), 10 + HEIGHT, 10, 10 + HEIGHT - (HEIGHT / num) * i)
    screen.update()
    screen.mainloop()

main()
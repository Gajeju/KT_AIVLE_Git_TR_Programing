import turtle
import random
 
def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
 
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
 
def draw_trapezoid(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(60)
    turtle.forward(height)
    turtle.right(120)
    turtle.forward(width+20)
    turtle.right(120)
    turtle.forward(height)
    turtle.right(60)
    turtle.end_fill()
 
 
def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
 
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
 
x = 0
y = 0
# 트리의 줄기를 그린다
draw_rectangle(t, "brown", x-20, y-50, 30, 50)
 
# 트리의 잎을 그린다
width = 240
height = 20
for i in range(12):
    width = width - 20
    x = 0 - width/2
    draw_trapezoid(t, "green", x, y, width, height)
    y = y + height

draw_circle(t, "yellow", -110, -20, 20)
t.penup()
t.goto(-125,-5)
t.write("Trend", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", -60, -15, 20)
t.penup()
t.goto(-70,0)
t.write("Git", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", -10, -10, 20)
t.penup()
t.goto(-20,5)
t.write("SQL", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", 40, -5, 20)
t.penup()
t.goto(30,10)
t.write("Infra", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", 90, 0, 20)
t.penup()
t.goto(77,15)
t.write("WEB", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", 70, 40, 20)
t.penup()
t.goto(55,50)
t.write("WAS", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", 20, 45, 20)
t.penup()
t.goto(3,57)
t.write("Cloud", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", -30, 50, 20)
t.penup()
t.goto(-47,58)
t.write("UI/UX", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", -80, 55, 20)
t.penup()
t.goto(-97,63)
t.write("JAVA", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", -50, 95, 20)
t.penup()
t.goto(-67,103)
t.write("Server", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", 0, 100, 20)
t.penup()
t.goto(-18,110)
t.write("Python", font=("Arial", 10, "italic"))

draw_circle(t, "yellow", 50, 105, 20)
t.penup()
t.goto(35,116)
t.write("Algorithm", font=("Arial", 8, "italic"))

draw_circle(t, "yellow", 20, 145, 20)
t.penup()
t.goto(0,160)
t.write("WebApp", font=("Arial", 8, "italic"))

draw_circle(t, "yellow", -30, 150, 20)
t.penup()
t.goto(-47,160)
t.write("mini P", font=("Arial", 10, "italic"))

draw_rectangle(t, "yellow", -80, 220, 160, 40)
t.penup()
t.goto(-75,230)
t.write("IT Service developer !", font=("Arial", 12, "italic"))


#14개 - 1.Trend/2.git/3.sql/4.infra/5.web/6.was/7.cloud/8.ui/ux
#9.java/10.server/11.python/12.algorithm/13.WebApp 14.mini P

t.penup()
t.color("black")
t.goto(-350, -260)
t.write("Merry Christmas !", font=("Arial", 24, "italic"))
t.goto(-350, -290)
t.write("Cheer up ! AIVLE SCHOOL !!", font=("Arial", 24, "italic"))

while True:
    pass

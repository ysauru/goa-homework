from turtle import *


speed(10)
width(5)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)

color("red")
begin_fill()
forward(100)
left(90)

right(180)
forward(70)

right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

right(150)
color("blue")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 130)
pendown()

color("yellow")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(130, 130)
pendown()

begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()
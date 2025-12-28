from turtle import *


speed(100)

width(6)
color("orange")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)    
end_fill()

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)    
forward(60)     
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
color("red")
begin_fill()
pendown()

right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
left(30)
forward(95)
color("blue")
begin_fill()
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(200,200)
forward(95)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




exitonclick()
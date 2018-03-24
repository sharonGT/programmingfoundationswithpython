import turtle


def draw_square():
     window = turtle.Screen()
     window.bgcolor("red")

     brad = turtle.Turtle()
     brad.shape("circle")
     brad.color("yellow")
     brad.speed(3)

     x = 0
     while x < 4: 
         brad.forward(100)
         brad.right(90)
         x = x + 1

     angie = turtle.Turtle()
     angie.shape("arrow")
     angie.color("blue")
     angie.circle(100)
     
     window.exitonclick()

draw_square()

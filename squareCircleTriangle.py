import turtle


def draw_auto(some_turtle):
    x = 0
    while x < 4:
        some_turtle.forward(100)
        some_turtle.right(90)
        x = x + 1

def draw_square():
     window = turtle.Screen()
     window.bgcolor("red")


     brad = turtle.Turtle()
     brad.shape("circle")
     brad.color("yellow")
     brad.speed(3)
     draw_auto(brad)
     
def draw_circle():
     window = turtle.Screen()
     window.bgcolor("red")
     angie = turtle.Turtle()
     angie.shape("arrow")
     angie.color("blue")
     angie.circle(100)



def draw_triangle():
     window = turtle.Screen()
     window.bgcolor("red")
     jen = turtle.Turtle()
     jen.shape("turtle")
     jen.color("green")
     i = 0
     while i < 3:
         jen.forward(300)
         jen.left(120)
         i = i + 1


     window.exitonclick()

draw_square()
draw_circle()
draw_triangle()

import turtle
def tortuga():

    turtle.shape("turtle")
    turtle.color('red', 'yellow')
    turtle.begin_fill()

    for i in range(5):
        
        turtle.forward(200)
        turtle.right(144)
        turtle.end_fill()
        turtle.done()
        

tortuga()
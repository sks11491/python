import turtle
turtleObj = turtle.Turtle()
turtleObj.fillcolor("green")
turtleObj.pencolor("red")
turtleObj.begin_fill()
while True:
    turtleObj.forward(200)
    turtleObj.right(108)
    if abs(turtleObj.pos()) < 1:
        break;
turtleObj.end_fill()
turtleObj.hideturtle()
turtle.done()
# Markus 11.11.26

#rõngad
import turtle



win = turtle.Screen()
win.setup(width=500, height=400)
win.title("Markus -  olümpiarõngad")
#liigutan õigessekohta
turtle.speed(0)
turtle.up()
turtle.goto(-150,50)
turtle.down()



#Ring 1
turtle.pensize(6)
turtle.pencolor("blue")
turtle.circle(50)

turtle.up()
turtle.goto(-40,50)
turtle.down()

#Ring 2
turtle.pensize(6)
turtle.pencolor("black")
turtle.circle(50)

turtle.up()
turtle.goto(70,50)
turtle.down()

#Ring 3
turtle.pensize(6)
turtle.pencolor("red")
turtle.circle(50)

turtle.up()
turtle.goto(20,-10)
turtle.down()


#Ring 4
turtle.pensize(6)
turtle.pencolor("green")
turtle.circle(50)

turtle.up()
turtle.goto(-100,-10)
turtle.down()


#Ring 5
turtle.pensize(6)
turtle.pencolor("yellow")
turtle.circle(50)










turtle.done()
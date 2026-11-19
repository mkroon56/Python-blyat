import turtle

# Aken
ekraan = turtle.Screen()
ekraan.setup(500, 500)
ekraan.title("Markus - Sinilill")

# Kilpkonn
t = turtle.Turtle()
t.speed("fastest")
t.pensize(10)

# Vars
t.color("green")
t.penup()
t.goto(0, -120)
t.pendown()
t.setheading(90)
t.forward(180)

# Leht
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
for _ in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

# Õis
t.penup()
t.goto(50, 120)
t.pendown()
t.color("blue", "lightblue")
t.begin_fill()
t.circle(55)
t.end_fill()

# Südamik
t.penup()
t.goto(15, 125)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(20)
t.end_fill()

t.hideturtle()

turtle.done()
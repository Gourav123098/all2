import turtle
from pygame import mixer
mixer.init()
mixer.music.load("preview.mp3")
mixer.music.set_volume(2.5)

#initiating___________________________________________________________________________________
wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor('#00001b')
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A____________________________________________________________________________________
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#b9fdff")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B_____________________________________________________________________________________
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#b9fdff")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball making________________________________________________________________________________
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#b9fdff")
ball.penup()
ball.goto(0,0)
ball.dx = 0.29
ball.dy = 0.29

# Pen________________________________________________________________________________________________
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#moving paddle_________________________________________________________________________________
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#keyborde__________________________________________________________________________________________________
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

score_a = 0
score_b = 0
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check____________________________________________________________
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor()>390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()<-390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # maoving ball according to player__________________________________________________________________
    if ball.xcor()>340 and (ball.ycor()< (paddle_b.ycor()+40)) and  (ball.ycor() > (paddle_b.ycor()-40)):
        # ball.setx(340)
        ball.dx *= -1
        mixer.music.play()

    if ball.xcor()<-340 and (ball.ycor()< (paddle_a.ycor()+40)) and  (ball.ycor() > (paddle_a.ycor()-40)):
        # ball.setx(-340)
        ball.dx *= -1
        mixer.music.play()
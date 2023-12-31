import turtle as t
import random
score=0
highscore=0
a=random.randint(-360,360)
b=random.randint(-260,260) 
wn=t.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.tracer(0)
wn.title("saanp wali game")

snk=t.Turtle()
snk.color("white")
snk.shape("square")
snk.penup()
snk.goto(350,0)



snk.direction="up"

eat=t.Turtle()
eat.shape("square")
eat.color("white")
eat.penup()
eat.goto(a,b)



if snk.direction!="down":
    snk.direction="up"
if snk.direction!="up":
    snk.direction="down"
if snk.direction!="left":
    snk.direction="right"


def up():
    
    if snk.direction!="down":
        snk.direction="up"
    
    
    
    
def down():
    if snk.direction!="up":
        snk.direction="down"
    
    
def left():
    if snk.direction!="right":
        snk.direction="left"
        
    
def right():
    if snk.direction!="left":
        snk.direction="right"

    
 

    
    
    


while True:
  
      
    c=random.randint(-360,360)
    d=random.randint(-260,260)
    
    wn.listen()
    wn.onkeypress(up,"w")
    wn.onkeypress(down,"s")
    wn.onkeypress(right,"d")
    wn.onkeypress(left,"a")
    if snk.xcor()>400:
        snk.setx(-400)
    if snk.xcor()<-400:
        snk.setx(400)
        
    if snk.ycor()>300:
        snk.sety(-300)
    if snk.ycor()<-300:
        snk.sety(300)
    
    if snk.direction=="up":
        y=snk.ycor()
        snk.sety(y+0.1)
    if snk.direction=="down":
        y=snk.ycor()
        snk.sety(y-0.1)
    if snk.direction=="right":
        x=snk.xcor()
        snk.setx(x+0.1)
    if snk.direction=="left":
        x=snk.xcor()
        snk.setx(x-0.1)
    
    
    if snk.xcor()<eat.xcor()+20 and snk.xcor()>eat.xcor()-20:
        if snk.ycor()<eat.ycor()+20 and snk.ycor()>eat.ycor()-20:
            eat.speed(0.5)
            eat.goto(c,d)
     
            

    

    wn.update()
    
   
    
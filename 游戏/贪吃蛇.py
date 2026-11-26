import turtle
import time
import random
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(600,600)
wn.tracer(0)
head=turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()
head.goto(0,0)
head.direction="stop"

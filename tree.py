import turtle, random

window = turtle.Screen()
turtle.screensize(1200, 1200)
window.bgcolor("MediumSeaGreen")

colors = ["red","green","FireBrick","Crimson","MediumVioletRed", "blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

t = turtle.Turtle(shape="arrow")

t.color(random.choice(colors))
t.lt(90)

lv = 10
l = 120
s = 26

t.width(lv)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def draw_tree(l, level):

  width = t.width() # save the current pen width

  t.width(width * 3.0 / 4.0) # narrow the pen width

  l = 3.0 / 4.0 * l

  t.lt(s)
  t.fd(l)

  if level < lv:
    draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)
    t.fd(l)
  t.color(random.choice(colors))
  if level < lv:
    draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)

  t.width(width) # restore the previous pen width

  t.speed("fastest")

draw_tree(l, 2)

def draw_square(zach):
  for i in range(1,7):
    zach.forward(50)
    zach.right(90)
    zach.left(750)
    zach.forward(50) 
def draw_art(): 
  #Create the turtle zach - draws a square
  zach = turtle.Turtle()
  zach.hideturtle()
  zach.penup()
  zach.goto(450, 350)
  zach.showturtle()
  zach.pendown()
  zach.shape("arrow")
  zach.speed(12)
  for i in range (1,73):
    zach.color(random.choice(colors))
    draw_square(zach)
    zach.right(5)
  #Create the turtle angie - draws a circle
  angie = turtle.Turtle()
  angie.hideturtle()
  angie.penup()
  angie.goto(450, 350)
  angie.showturtle()
  angie.pendown()
  angie.shape("arrow")
  angie.color("blue")
  angie.circle(70)
  angie.speed(11)
  for i in range (1,73):
    angie.circle(70)
    angie.right(5)
  #Create the turtle jane - draws a circle
  jane = turtle.Turtle()
  jane.hideturtle()
  jane.penup()
  jane.goto(450, 350)
  jane.showturtle()
  jane.pendown()
  jane.shape("arrow")
  jane.color("yellow")
  jane.circle(50)
  jane.speed(11)
  for i in range (1,73):
    jane.circle(50)
    jane.right(5)

draw_art()

window.exitonclick()

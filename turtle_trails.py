shape="ꆜ"
# count variable for each fruit
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
# count variable so that NPC's only interact with the player once
check1=0
check2=0
check3=0
check4=0
check5=0
check6=0
# time control variable
t1=0
t2=0

# import turtle and time packages
import turtle
import time

# create screen object 
sc = turtle.Screen() 
   
# create turtle object 
pen = turtle.Turtle()
pen2= turtle.Turtle()
apple1=turtle.Turtle()
apple1.hideturtle()
apple1.up()
apple2=turtle.Turtle()
apple2.hideturtle()
apple2.up()
apple3=turtle.Turtle()
apple3.hideturtle()
apple3.up()
apple4=turtle.Turtle()
apple4.hideturtle()
apple4.up()
apple5=turtle.Turtle()
apple5.hideturtle()
apple5.up()
apple6=turtle.Turtle()
apple6.hideturtle()
apple6.up()
apple7=turtle.Turtle()
apple7.hideturtle()
apple7.up()
apple1.shape("circle"), apple2.shape("circle"), apple3.shape("circle"), apple4.shape("circle"), apple5.shape("circle"), apple6.shape("circle"), apple7.shape("circle")
apple1.color("Plum"), apple2.color("Plum"), apple3.color("Plum"), apple4.color("Plum"), apple5.color("Plum"), apple6.color("Plum"), apple7.color("Plum")
pen2.up()
pen2.hideturtle()
pen2.setpos(-85,-255)

# set position of the turtle
pen.up()
pen.setpos(-100,-100)

# method to draw square 
def draw(): 
   
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
   
  pen.forward(30) 
   
if __name__ == "__main__" :
  
    # set turtle object speed 
    pen.speed(0)
       
    # loops for board 
    for i in range(8): 
       
      # not ready to draw 
      pen.up() 
       
      # set position for every row 
      pen.setpos(-100, 30 * i) 
       
      # ready to draw 
      pen.down() 
       
      # row 
      for j in range(8):

        col="Turquoise"
             
        # fill with given color 
        pen.fillcolor(col) 
       
        # start filling with colour 
        pen.begin_fill() 
       
        # call method 
        draw()
        
        # stop filling 
        pen.end_fill()

    # not ready to draw
    pen.up()

    # move the turtle to initial game position
    pen.setpos(-85,15)

    # turn the turtle to face the correct direction
    pen.left(90)

    # setting the colour of the turtle
    pen.color("Black")

    # functions for player movements
    def stopit():
      turtle.bye()

    def turnleft():
      pen.left(90)

    def turnright():
      pen.right(90)

    def forward():
      turtle.delay(10)
      pen.forward(30)
      # check if the player is in any NPC's vicinity
      if pen.xcor()>-100 and pen.xcor()<-70 and pen.ycor()>60 and pen.ycor()<90:
        npc1doesstuff()
      elif pen.xcor()>-70 and pen.xcor()<-40 and pen.ycor()>180 and pen.ycor()<210:
        npc2doesstuff()
      elif pen.xcor()>-40 and pen.xcor()<-10 and pen.ycor()>60 and pen.ycor()<90:
        npc3doesstuff()
      elif pen.xcor()>50 and pen.xcor()<80 and pen.ycor()>30 and pen.ycor()<60:
        npc4doesstuff()
      elif pen.xcor()>20 and pen.xcor()<50 and pen.ycor()>120 and pen.ycor()<150:
        npc5doesstuff()
      elif pen.xcor()>70 and pen.xcor()<100 and pen.ycor()>150 and pen.ycor()<180:
        npc6doesstuff()

    def turnleft2():
      pen2.left(90)

    def turnright2():
      pen2.right(90)

    def forward2(): 
      global t1
      global t2
      turtle.delay(10)
      pen2.forward(30)
      if pen2.xcor()>-56 and pen2.xcor()<-54 and pen2.ycor()>-256 and pen2.ycor()<-254:
        global count1, count2, count3, count4, count5, count6, count7
        count1+=1
        apple1.hideturtle()
        t2=time.time()
      elif pen2.xcor()>-26 and pen2.xcor()<-24 and pen2.ycor()>-106 and pen2.ycor()<-104:
        count2+=1
        apple2.hideturtle()
        t2=time.time()
      elif pen2.xcor()>124 and pen2.xcor()<126 and pen2.ycor()>-136 and pen2.ycor()<-134:
        count3+=1
        apple3.hideturtle()
        t2=time.time()
      elif pen2.xcor()>64 and pen2.xcor()<66 and pen2.ycor()>-76 and pen2.ycor()<-74:
        count4+=1
        apple4.hideturtle()
        t2=time.time()
      elif pen2.xcor()>-86 and pen2.xcor()<-84 and pen2.ycor()>-46 and pen2.ycor()<-44:
        count5+=1
        apple5.hideturtle()
        t2=time.time()
      elif pen2.xcor()>4 and pen2.xcor()<6 and pen2.ycor()>-166 and pen2.ycor()<-164:
        count6+=1
        apple6.hideturtle()
        t2=time.time()
      elif pen2.xcor()>94 and pen2.xcor()<96 and pen2.ycor()>-226 and pen2.ycor()<-224:
        count7+=1
        apple7.hideturtle()
        t2=time.time()
      if (count1>0 and count2>0 and count3>0 and count4>0 and count5>0 and count6>0 and count7>0 and (t2-t1)<=20):
        print("You win!")
        count=0
      if (count1>0 and count2>0 and count3>0 and count4>0 and count5>0 and count6>0 and count7>0 and (t2-t1)>20):
        print("You collected all the fruits. Unfortunately, not in time...")

    # set keyboard bindings
    turtle.listen()
    # restrict NPC 1 to interact during setting up of minigame map
    if check1!=1:
      turtle.onkey(turnleft,"a")
    if check1!=1:
      turtle.onkey(turnright,"d")
    if check1!=1:
      turtle.onkey(forward,"w")
    turtle.onkey(stopit,"space")
    turtle.onkey(turnleft2,"j")
    turtle.onkey(turnright2,"l")
    turtle.onkey(forward2,"i")

    # create NPC's
    npc1= turtle.Turtle()
    npc2= turtle.Turtle()
    npc3= turtle.Turtle()
    npc4= turtle.Turtle()
    npc5= turtle.Turtle()
    npc6= turtle.Turtle()

    # provide attributes to the NPC's
    npc1.up(), npc2.up(), npc3.up(), npc4.up(), npc5.up(), npc6.up()

    npc1.shape("turtle"), npc2.shape("turtle"), npc3.shape("turtle"), npc4.shape("turtle"), npc5.shape("turtle"), npc6.shape("turtle")
    
    npc1.shapesize(0.7,0.6,0.5), npc2.shapesize(0.7,0.6,0.5), npc3.shapesize(0.7,0.6,0.5), npc4.shapesize(0.7,0.6,0.5), npc5.shapesize(0.7,0.6,0.5), npc6.shapesize(0.7,0.6,0.5)

    npc1.color("Yellow"), npc2.color("Pink"), npc3.color("Red"), npc4.color("Purple"), npc5.color("Green"), npc6.color("Blue")
    
    npc1.speed(1), npc2.speed(1), npc3.speed(1), npc4.speed(1), npc5.speed(1), npc6.speed(1)

    npc2.setpos(-45,195), npc4.setpos(70,35), npc5.setpos(45,130), npc1.setpos(-90,80), npc6.setpos(105,165), npc3.setpos(-30,65)

    # interact with NPC's 
    def npc1doesstuff():
      global check1
      global t1
      # work only the first time NPC1 is called
      if check1==0:
        print("Welcome, I am Amberis.\nI have been awaiting a worthy challenger for aeons!\nYou must collect all ethereal fruits before time runs out in order to win.\nYour challenge lies ahead!")
        check1=1
        npc1.hideturtle(), npc2.hideturtle(), npc3.hideturtle(), npc4.hideturtle(), npc5.hideturtle(), npc6.hideturtle()
        pen2.showturtle()
        pen2.color("Magenta")
        pen2.up()
        pen2.speed(0)
        # set up minigame 1 map 
        for i in range(8):  
          pen2.up()  
          pen2.setpos(-100, (-270 + 30*i)) 
          pen2.down() 
          for j in range(8):
            col="Yellow" 
            pen2.fillcolor(col)  
            pen2.begin_fill() 
            for i in range(4):
              pen2.forward(30)
              pen2.left(90)
            pen2.forward(30) 
            pen2.end_fill()
        pen2.up()
        pen2.setpos(-85,-255)
        pen2.color("Magenta")
        apple1.setpos(-55,-255), apple2.setpos(-25,-105), apple3.setpos(125,-135), apple4.setpos(65,-75), apple5.setpos(-85,-45), apple6.setpos(5,-165), apple7.setpos(95,-225)
        apple1.shapesize(0.7,0.6,0.5), apple2.shapesize(0.7,0.6,0.5), apple3.shapesize(0.7,0.6,0.5), apple4.shapesize(0.7,0.6,0.5), apple5.shapesize(0.7,0.6,0.5), apple6.shapesize(0.7,0.6,0.5), apple7.shapesize(0.7,0.6,0.5) 
        apple1.showturtle(), apple2.showturtle(), apple3.showturtle(), apple4.showturtle(), apple5.showturtle(), apple6.showturtle(), apple7.showturtle()
      t1=time.time()
      
    def npc2doesstuff():
      global check2, check1
      # restrict other NPC's to interact during setup of minigame
      if check2==0 and check1!=1:
        print("Insert Pink's dialogue")
      check2=1

    def npc3doesstuff():
      global check3, check1
      if check3==0 and check1!=1:
        print("Insert Red's dialogue")
      check3=1

    def npc4doesstuff():
      global check4, check1
      if check4==0 and check1!=1:
        print("Insert Purple's dialogue")
      check4=1

    def npc5doesstuff():
      global check5, check1
      if check5==0 and check1!=1:
        print("Insert Green's dialogue")
      check5=1

    def npc6doesstuff():
      global check6, check1
      if check6==0 and check1!=1:
        print("Insert Blue's dialogue")
      check6=1

    # driver code
    while True:
      pen.forward(0)
      
      # keep the player within the map
      if pen.xcor()>140 or pen.xcor()<-100:
        pen.right(180)
        pen.forward(30)
        print("Bonk! Go back inside the map")
        # double check if player is within the map incase they spam press forward key
        if pen.xcor()>130 or pen.xcor()<-90:
          pen.setpos(-85,15)
          print("You have been returned to the initial position for repeatedly trespassing.")

      elif pen.ycor()>240 or pen.ycor()<0:
        pen.right(180)
        pen.forward(30)
        print("Bonk! Go back inside the map")
        if pen.ycor()>-40 or pen.ycor()<280:
          pen.setpos(-85,15)
          print("You have been returned to the initial position for repeatedly trespassing.")
          
      # keep the player within the minigame map
      if pen2.xcor()>140 or pen2.xcor()<-100:
        pen2.right(180)
        pen2.forward(30)
        print("You mustn't disrupt the quest! Finish what you started.")
        if pen2.xcor()>130 or pen2.xcor()<-90:
          pen2.setpos(-85,-255)
          print("You have been returned to the initial position for trying to escape the battle.")
      
      elif pen2.ycor()>-30 or pen2.ycor()<-270:
        pen2.right(180)
        pen2.forward(30)
        print("You mustn't disrupt the quest! Finish what you started.")
        if pen2.ycor()>-40 or pen2.ycor()<-280:
          pen2.setpos(-85,-255)
          print("You have been returned to the initial position for trying to escape the battle.")
      


      

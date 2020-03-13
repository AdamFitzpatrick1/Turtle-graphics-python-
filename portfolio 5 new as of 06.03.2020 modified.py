#Python turtle graphics animation
import turtle
import time 
screen = turtle.Screen()
t = turtle.Turtle()
screen.tracer(0) 
sizescreen = 1000
screen.setup(sizescreen,sizescreen)
t.penup()
def drawA():

    #Draws the A 
       t.pendown() 
       t.right(70)
       t.forward(50)    
       t.backward(50)
       t.right(45)
       t.forward(50)
       t.backward(25)
       t.right(245)
       t.forward(30)
       t.penup()
       t.forward(5)
  

def drawF():

    #Draws the F 
        t.pendown()
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(50) 
        t.backward(50)
        t.forward(50)
        t.right(180)
        t.forward(50)
        t.right(270)
        t.pendown()
        t.forward(25)
        t.right(-90)
      
        t.forward(30)
        t.penup()

#Draw stickman

def stickman(xp, yp):

        x = xp
        y = yp
        headSize = 25
        ninetyDegree = 90
        thirtypixels = 30
        minusseventy = -70
        minusonetwenty = -120
        leftminustwothirty = -230
        forwardfifthteen = 15
        minusoneeightyright = -180
        oneeightyleft = 180
        forwardfifty = 50 
        minusfiftyforward = -50
        forwardeighty = 80
        widthbetween = 70
      


        t.goto(x,y)
        t.pendown();
        t.circle(headSize)
        t.right(ninetyDegree)
        t.forward(thirtypixels)
        t.left(minusseventy)
        t.forward(thirtypixels)
        t.backward(thirtypixels)
        t.right(minusonetwenty)
        t.forward(thirtypixels)
        t.backward(thirtypixels)
        t.left(leftminustwothirty)
        t.penup();
        t.forward(forwardfifthteen)
        t.pendown()
        t.penup()
        t.right(ninetyDegree)
        t.forward(thirtypixels)
        t.right(minusoneeightyright)
        t.forward(thirtypixels)
        t.forward(thirtypixels)
        t.left(oneeightyleft)
        t.pendown()
        t.forward(forwardfifty)
                
        t.forward(minusfiftyforward)
        
       
        
        t.penup()
     
                
                
        x = x + widthbetween
        t.setx(x)
        t.sety(y)
        
x = 90
y = 90  

#Draw stickman but keep them static (not animated)
def stickmanstatic():
    x = -60
    y = -60
    for i in range(0,6):


        t.goto(x,y)
        t.pendown();
        t.circle(25) #head 
        t.right(90)
        t.forward(30)
        t.left(-70)
        t.forward(30)
        t.backward(30)
        t.right(-120)
        t.forward(30)
        t.backward(30)
        t.left(-230)
        t.penup();
        t.forward(15)
        t.pendown()
        t.right(90)
        t.forward(30)
        t.backward(60)
        
      
        
        t.penup()
   
        
        x = x + 70
        
        t.setx(x)
        t.sety(y)
       

speedy = 15
speedx = 20 

while True:

        t.clear()
        #Draw stuff in here
        drawA()
        drawF()
        stickman(x, y)
        stickmanstatic()
        time.sleep(0.1)
        screen.update()
        #Do maths here 
        x =  x + speedx
        y =  y + speedy
        if y >  300 or y < -300:
                speedy = speedy * -1
                

        if x >  300 or x < -300:
                speedx = speedx * -1 
    
        
        
       

      
        
        
       






import pgzrun,random
from time import time

satcur=0
timeofgame=time()
timetot=0
linedets=[]
WIDTH=618
HEIGHT=411
satalitetotal=10
gameover=False

satall=[]
for i in range(satalitetotal):
   sat=Actor("needle14")
   sat.pos=(random.randint(30,600),random.randint(30,400))
   satall.append(sat)

def draw():
   global timetot,satcur,timeacc
   screen.blit("hay14",(0,0))
   for i,j in enumerate(satall,1):
      j.draw()
      screen.draw.text(str(i),(j.pos[0],j.pos[1]+20),color=(247,8,255))
   if satcur<satalitetotal:
    timetot=time()-timeofgame
    timeacc=30-timetot
    screen.draw.text(str(round(timeacc,2)),(20,20),fontsize=30,color=(247,8,255))
   else:
     screen.draw.text(str(round(timetot,2)),(20,20),fontsize=50,color=(247,8,255)) 
     screen.draw.text("You are inhumane",(30,100),fontsize=100,color=(247,8,255))
   if gameover:
      screen.fill((89,67,54))
        
   
   for i in linedets:
      screen.draw.line(i[0],i[1],(247,8,255))

def update():
   pass

def timeup():
   global gameover
   gameover=True

      

def on_mouse_down(pos):
   global satcur,linedets
   if satcur<satalitetotal:
      if satall[satcur].collidepoint(pos):
         if satcur:
            linedets.append((satall[satcur-1].pos,satall[satcur].pos))
         satcur+=1
      else:
         linedets=[]
         satcur=0

   
clock.schedule(timeup,30)
pgzrun.go()


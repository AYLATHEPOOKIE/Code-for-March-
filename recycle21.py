import pgzrun, random
WIDTH=800
HEIGHT=600
curlevel=1
levels=10
anim=[]
speed=10
gamewin=False
gamelose=False
badstuff=["bag","battery","bottle","chips"]
stagedis=[]

def draw():
    screen.fill((144,212,142))
    if gamelose:
        screen.draw.text("Recycle plsss come again",fontsize=50,color=((33,18,64)))
    elif gamewin:
        screen.draw.text("yaay!",fontsize=50,color=((33,18,64)))
    else:
        for i in stagedis:
            i.draw()

def update():
    global stagedis
    if len(stagedis)==0:
        stagedis=master(curlevel)

def master(r):
    thestage=popul(r)
    theactors=accimage(thestage)
    layout(theactors)
    ani(theactors)
    return theactors


def popul(r):
    thestage=["paper"]
    for i in range(r):
        ran=random.choice(badstuff)
        thestage.append(ran)
    return thestage

def accimage(thestage):
    theactors=[]
    for i in thestage:
        thing=Actor(i)
        theactors.append(thing)
    return theactors

def layout(y):
    noofgaps=len(y)+1
    gapsize=800/noofgaps
    random.shuffle(y)
    for i,j in enumerate(y,1):
        xpos=i*gapsize
        j.x=xpos
    

def ani(smoothmotion):
    global anim
    for i in smoothmotion:
        dur=speed-curlevel
        i.anchor=("center","bottom")
        animation=animate(i,duration=dur,on_finished=gameislost,y=600)
        anim.append(animation)

def gameislost():
    global gamelose
    gamelose=True

def gameiswin():
    global gamewin,stagedis,anim
    stopanim()
    if curlevel==levels:
        gamewin=True
    else:
        curlevel+=1
        stagedis=[]
        anim=[]

def stopanim(hi):
    for i in hi:
        if i.running:
            i.stop()

def on_mouse_down(pos):
    for i in stagedis:
        if i.collidepoint(pos):
            if "bag" in i.image:
                gameiswin()
            else:
                gameislost()


pgzrun.go()
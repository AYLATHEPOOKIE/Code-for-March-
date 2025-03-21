import pgzrun, random
WIDTH=800
HEIGHT=600
levels=10
gamewin=False
gamelose=False
badstuff=["bag","battery","bottle","chips"]
stagedis=[]

def draw():
    screen.fill((144,212,142))
    if gamelose:
        screen.draw("Recycle plsss come again",fontsize=50,color=((33,18,64)))
    elif gamewin:
        screen.draw("yaay!",fontsize=50,color=((33,18,64)))
    else:
        for i in stagedis:
            i.draw()

def update():
    pass



pgzrun.go()
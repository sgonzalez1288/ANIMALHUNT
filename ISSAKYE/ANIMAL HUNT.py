from gamelib import *

game=Game(800,600,"Animal Hunt")
bk=Image("images\\FOREST.jpg",game)
bk.resizeTo(game.width,game.height)
boar=Image("images\\BOAR.png",game)
boar.resizeBy(-75)
boar.setSpeed(2,40)
person=Image("images\\JESUS.png",game)
person.resizeBy(-70)
crosshair=Image("images\\crosshair2.png",game)
crosshair.resizeBy(0)
gameover=Image("images\\gameover.png",game)
gun= Sound("sound\\Gun2.wav",1)
pain=Sound("sound\\PAIN.wav",1)
pig=Sound("sound\\PIGS.wav",1)
bk.draw()
boar.draw()
crosshair.draw()



jumping= False
landed= False
factor= 1

game.drawText("Animal Hunt",game.width/4 ,game.height/4,Font(red,90,yellow))
game.drawText("USE W,A,S,D TO MOVE,MOUSE1 TO SHOOT THE PIG",game.width/8.5 ,game.height/1.5,Font(red,36,yellow))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_SPACE)

oj=Animation("images\\OJ.png",1,game,832,1163)
oj.resizeBy(-35)
x = randint(50, 590)
y = -100
oj.moveTo(x, y)
oj.setSpeed(2, 180)
oj.resizeBy(-90)


while not game.over:
    game.processInput()
    bk.draw()
    boar.draw()
    crosshair.draw()
    oj.move()
    boar.move(True)
    person.move(True)
    crosshair.moveTo(mouse.x,mouse.y)


    if oj.isOffScreen("bottom"):
        x = randint(50, 590)
        y = -100
        oj.moveTo(x, y)
        
    if keys.Pressed[K_a]:
        person.x -=3
    elif keys.Pressed[K_d]:
        person.x +=3

    else:
        person.draw()
        
    if keys.Pressed[K_s]:
        person.y +=3
    if person.y >300:
        landed=True
    if jumping:
        person.y -= 24 * factor
        factor *= .95
        landed = False
        
        if factor < .18:
            jumping = False
            factor = 1
            
    if keys.Pressed[K_w] and landed and not jumping:
        jumping = True
    if not landed:
        person.y += 9
    if boar.collidedWith(mouse)and mouse.LeftButton:
        xCoordinate=randint(150,650)
        yCoordinate=randint(150,450)
        boar.moveTo(xCoordinate,yCoordinate)
        game.score +=10
        pig.play()
    if boar.collidedWith(person):
        xCoordinate=randint(150,650)
        yCoordinate=randint(150,450)
        boar.moveTo(xCoordinate,yCoordinate)
        game.score -=10
        
    if person.collidedWith(mouse)and mouse.LeftButton:
        xCoordinate=randint(150,650)
        yCoordinate=randint(150,450)
        person.moveTo(xCoordinate,yCoordinate)
        person.health -=10
        pain.play()
    if person.collidedWith(oj):
        x = randint(50, 590)
        y = -100
        oj.moveTo(x, y)
        person.health +=10
    if person.health<10:
        game.over= True
    if person.health>=100 and game.score >=100:
        game.over= True 
        xCoordinate=randint(100,700)
        yCoordinate=randint(100,500)
        person.moveTo(xCoordinate,yCoordinate)
        person.health -=10
    if mouse.LeftButton:
        gun.play()

    if game.over:
        gameover.draw()
        
    
    game.drawText("Health:" + str(person.health),200,5)

    game.displayScore()
    game.update(120)
game.drawText("Press [SPACE] to Exit",320, 400)
game.wait(K_SPACE)
game.quit()




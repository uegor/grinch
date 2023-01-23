#for pc
from pygame import*
import time as r
from random import randint

font.init()
w,h = 1920,1080

class Grinch:
    def __init__(self,health,filename,c,d,x,y): 
        self.image = image.load(filename)
        self.image = transform.scale(self.image, [c,d])
        self.image_tooshonka = self.image
        self.d = d
        self.c = c
        self.x = x
        self.y = y
        self.tts = 1
        self.health = health
        self.csgo = False
        self.font = font.Font(None,40)
        self.label =  self.font.render( str(self.health),True,(255,0,0)    )
        self.hp_bar = Rect(x, y, c, 10)
    def draw(self):
        win.blit(self.image_tooshonka, [self.x,self.y])
    def draw_hp_bar(self):
        draw.rect(win, (255,0,0), self.hp_bar)
        self.label =  self.font.render( str(self.health),True,(0,0,0))
        win.blit(self.label, (self.x+250,self.y))
    def laser (self):
        if self.csgo:
            if len(lasers)< 5:
                Laser(self.x,randint(0,h))
                self.csgo = False
            else:
                lasers.pop(0)
                
    def colodde(self,cat):
        self.rect = Rect(self.x,self.y,self.c,self.d) 
        cat.rect = Rect(cat.x,cat.y,cat.c,cat.d)
        if self.rect.colliderect(cat.rect):
            self.health -= 20
            cat.x = 0 
class  Pr:
    presents = []

    def __init__(self,filename,c,d): 
        
        self.image = image.load(filename)
        self.image = transform.scale(self.image, [c,d])
        self.d = d
        self.c = c
        self.x = randint(0, w)
        self.y = randint(0, h) 
        Pr.presents.append(self)

    def draw(self):
        win.blit(self.image, [self.x,self.y]) 
        


class Animal:
    def __init__(self,name,breed,weight,gender,health,filename,c,d,x,y): 
        self.name = name
        self.image = image.load(filename)
        self.image = transform.scale(self.image, [c,d])
        self.image_tooshonka = self.image
        self.d = d
        self.c = c
        self.x = x
        self.y = y 
        self.breed = breed
        self.weight = weight
        self.gender = gender
        self.health = health
        self.live = True

    def hbl (self):
        self.health -=1 
        if  self.health < 0:
            global mode
            mode = "end"
    def died (self):
        self.live = False

    def draw(self):
        if self.live:
            win.blit(self.image_tooshonka, [self.x,self.y]) 
    
    def run(self,m):
        self.x += m
 
    def up(self,m):
        self.y -= m
 
class Dog(Animal):
    touch=False
    face = 'right'

    def move(self,cat):
        if self.live:
            if self.x > cat.x:
                dx = abs(self.x - cat.x)
                self.x -= dx/50
            else:
                dx = abs(cat.x - self.x)
                self.x += dx/50
    
            if self.y > cat.y:
                dy = self.y - cat.y
                self.y -= dy/50
            else:
                dy = cat.y - self.y
                self.y += dy/50
            cat.colidde(self)

    def patr(self,cat):
        if self.live:
            if self.face == "right":
                self.x += 5
                if self.x + self.c> w:
                    self.face = "left"
            if self.face == "left":
                self.x -= 5
                if self.x<0:
                    self.face = "right"
            cat.colidde(self)

class Cat(Animal):
    def __init__(self,name,breed,weight,gender,health,filename,c,d,x,y,scary):
        super().__init__(name,breed,weight,gender,health,filename,c,d,x,y,)
        self.scary = scary
        self.scary_image = image.load(scary)
        self.scary_image = transform.scale(self.scary_image, [c,d])
        self.touch = False
        self.font = font.Font(None,20)
        self.label =  self.font.render( str(self.health),True,(255,0,0)    )
        self.hp_bar = Rect(x, y, c, 10)
    
    def control(self): 
        keys = key.get_pressed()
        if keys[K_d]: self.run(5)
        if keys[K_a]: self.run(-5)
        if keys[K_w]: self.up(3)
        if keys[K_s]: self.up(-3)
        if self.x  < 0:
            self.x = 0 
        if self.x + self.c > w:
            self.x = w - self.c
 
        if self.y + self.d > h:
            self.y = h - self.d 
        if self.y  < 0:
            self.y = 0   

    def run(self,m):
        self.x += m
        self.hp_bar = Rect(self.x, self.y-10, self.c, 10)
 
    def up(self,m):
        self.y -= m
        self.hp_bar = Rect(self.x, self.y-10, self.c, 10)
 
    def draw_hp_bar(self):
        draw.rect(win, (255,0,0), self.hp_bar)
        self.label =  self.font.render( str(self.health),True,(0,0,0))
        win.blit(self.label, (self.x+50,self.y-10))
    def colidde(self,dog):
        self.rect = Rect(self.x,self.y,self.c,self.d) 
        dog.rect = Rect(dog.x,dog.y,dog.c,dog.d) 
        if self.rect.colliderect(dog.rect):
            self.image_tooshonka = self.scary_image
            if self.touch:
                end = r.time()
                if end- self.start>2:
                    global mode
                    mode = 'end'
            else:
                self.start = r.time()
                self.touch=True                  
        else:
            for dog in dogs:
                dog.rect = Rect(dog.x,dog.y,dog.c,dog.d)
                if self.rect.colliderect(dog.rect):
                    self.touch=True
                    
                    break
            else:
                self.touch=False
                self.start = r.time()
            if not self.touch:   
                self.image_tooshonka = self.image
                self.touch=False

class Tel:
    def __init__(self,c,d,x,y,l_n):   
        self.d = d
        self.l_n = l_n
        self.c = c
        self.x = x
        self.y = y
        self.font = font.Font(None,94)
        self.label =  self.font.render("уровень " + str(l_n),
                            True,(255,0,0)    )
        self.active = False 

    def draw (self):
        if self.active:
            draw.rect(win, (255,0,0), 
                Rect(self.x,self.y,self.c,self.d),width=5)
            win.blit(self.label,(self.x+100,self.y-70))

    def colodde(self,cat):
        self.rect = Rect(self.x,self.y,self.c,self.d) 
        cat.rect = Rect(cat.x,cat.y,cat.c,cat.d)
        if self.active == True:
            if self.rect.colliderect(cat.rect):
                self.active = 0
                global bg,level,time_tagger
                time_tagger=0
                if self.l_n == 2:
                    level = self.l_n
                    bg = image.load('room.jpg')
                    bg = transform.scale(bg,[w,h])

class Laser:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.h = randint(10,30)
        lasers.append(self) 
    def draw(self):     
        draw.rect(win, (255,0,0), Rect(0,self.y,self.x,self.h))

    def colide(self,aim):
        self.rect = Rect(0,self.y,self.x,self.h) 
        aim.rect = Rect(aim.x,aim.y,aim.c,aim.d) 
        if self.rect.colliderect(aim.rect):
            if aim.name == "bonya":
                aim.hbl()
               
            else:
                aim.died()

t=Cat(name='anfisa',breed='britian',weight=2, gender='кошка',health=100,filename='ccc (1).png',c=150,d=100,x=360,y=800,scary="s (2).png")                                 

bobik = Dog(name='bobik',breed='shiba inu',weight=7,gender='собака',health=220,filename='d (1).png',c=150,d=100,x=900,y=700)                                                 

patrol = Dog(name='patrolk',breed='shiba inu',weight=7,gender='собака',health=220,filename='d (1).png',c=150,d=100,x=750,y=850)

b=Cat(name='bonya',breed='britian chincila',weight=5,gender='кот',health=150,filename='cc (5).png',c=110,d=80,x=600,y=525,scary="s (2).png")

pot = Dog(name='patrolk',breed='shiba inu',weight=7,gender='собака',health=220,filename='d (1).png',c=150,d=100,x=650,y=750)

hehehaha = Grinch (health=100, filename="gg.jpg", c=0.3*w, d=h, x=0.7*w, y=0) 

dogs = [bobik,patrol,pot] 

lasers = []

time_tagger = 0 

level2 = Tel(c = 550, d=420 , x=w-550, y=h-418, l_n=2)

level3 = Tel (c = 550, d=420 , x=w-550, y=h-418, l_n=3)
 
win = display.set_mode([w,h])

bg = image.load('room.png')
bg = transform.scale(bg,[w,h])
end_bg = image.load('u.jpg')
end_bg = transform.scale(end_bg,[w,h])
mode = "game"
level = 1
clock = time.Clock()
 
def mainloop():
    while True:
        global time_tagger
 
        clock.tick(60)
        time_tagger += 1/30
        
        for doom in event.get():
            if doom.type == QUIT: exit()
            if mode == "end" and doom.type == KEYDOWN and doom.key == K_ESCAPE: exit()
 
        if mode == "game":
            win.blit(bg,[0,0])
            if level == 1:
                level2.draw()
                level2.colodde(b)
                if time_tagger/60 > 0.30: level2.active = True
                hehehaha.draw()
                hehehaha.colodde(b)
                hehehaha.draw_hp_bar()
                if int(time_tagger) == int (hehehaha.tts) :
                    hehehaha.csgo = True
                    hehehaha.laser()
                    hehehaha.tts += 0.1
                    Pr('pr.png',100, 100)

                for laser in lasers:
                    laser.draw()
                    laser.colide(b)
                    for dog in dogs:
                       laser.colide(dog) 

            if level == 2:
                level3.draw()
                level3.colodde(b)
                if time_tagger/60 > 0.30: level3.active = True
                        
            pot.draw()
            pot.patr(b)
            patrol.draw()
            patrol.patr(b)
            b.draw()
            b.draw_hp_bar()
            bobik.draw()
            t.draw()
            b.control()
            bobik.move(b)

            for pr in Pr.presents:
                pr.draw()
 
        if mode == "end":
            win.blit(end_bg,[0,0])
 
        display.update()
 
mainloop()    
# полоска со здоровьем  
# подарки со здоровьем
# добавить урон

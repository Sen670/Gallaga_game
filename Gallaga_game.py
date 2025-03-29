import pgzrun 
import random 

WIDTH = 1000
HEIGHT = 700

ship = Actor("spaceship")
ship.pos = (200,400)
enemies = []
bullets = []
score = 0 

for i in range(8):
    for j in range(4):
        bug = Actor("bee")
        enemies.append(bug)
        enemies[-1].x = 100 + 50 * i
        enemies[-1].y = 80 + 50 * j



WHITE = (255,255,255)
BLUE = (0,0,255)

def draw(): 
    screen.clear()
    screen.fill(BLUE) 
    for i in enemies:
        i.draw()
        
    ship.draw() 
 
    for i in bullets:
        i.draw()
    

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x 
        bullets[-1].y = ship.y - 100
        

def display_score():
        screen.draw.text("Score:"+str(score),(100,200),color = "white",fontsize = 50)

def game_over(): 
     global score
     screen.draw.text("GAME OVER! Your final score is:",(score))
     
def update():
     if keyboard.left:
          ship.x -= 10
     
     if keyboard.right:
          ship.x += 10

     for i in bullets:
          if i.y <= 0:
               bullets.remove(i)
          else:
             i.y -= 10
          


   




pgzrun.go()   
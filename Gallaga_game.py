import pgzrun 
import random 

WIDTH = 1000
HEIGHT = 700

ship = Actor("spaceship")
ship.pos = (200,400)
enemies = []
bullets = []

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
    




   

pgzrun.go()   
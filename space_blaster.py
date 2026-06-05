# importing the modules
import turtle, time, pygame, random, sys, _tkinter

# intialising the mixer
pygame.mixer.init()

game_ended = False
game_over = False

# creating our architect turtles
archy = turtle.Turtle()

archybro = turtle.Turtle()
otherarch = turtle.Turtle()

otherarch.penup()
otherarch.hideturtle()
otherarch.goto(320, 218)
otherarch.pencolor('white')
otherarch.write("×",align=('center'), font=("BankGothic", 10,"bold"))

archybro.penup()
archybro.hideturtle()
archybro.pencolor('red')
archybro.goto(357, 215)

def shoot_bullet():
    global spship
    global bullet
    
    if bullet.isvisible() == False:
        bullet.goto(spship.xcor()-1, spship.ycor()+39.75)
        bullet.showturtle()
                
        laser_sounds = ["assets/laser.wav","assets/pew.mp3","assets/laserzap.mp3","assets/sew.mp3","assets/lasergun.mp3"]
        laser_sound = pygame.mixer.Sound(random.choice(laser_sounds))
        laser_sound.set_volume(0.8)
        laser_sound.play()
        
def game_isover():
    global game_ended
    global archy
    game_over = True
    pygame.mixer.music.stop()
    try: 
        turtle.onkey(None, 'Escape')
    except turtle.Terminator:
        print('Thanks for playing!')
        sys.exit()
    
    archy.penup()
    archy.home()
    archy.pencolor('white')
    
    archy.write("GAME OVER",align=('center'), font=("BankGothic", 70,"bold"))
    archy.right(90)
    archy.forward(75)  
    
    archy.pencolor('orange')
    archy.write("Good job! Now, click to exit", align=('center'), font=("Orbitron Regular", 20,"italic"))
    archy.hideturtle() 
    
    turtle.exitonclick()

# setting the window
win = turtle.Screen()
win.setup(800, 600)
win.bgpic('assets/space-bg.gif')
win.title('Space Blaster')
win.tracer(0)

enemy_list = []
try:
    enems = int(win.numinput('Enter the no. of enemies you want to face', 'No. of Enemies', minval = 5, maxval = 60))
except TypeError:
    print('\nThanks for playing!')
    sys.exit()

def leftkeypress():
    global moveShip
    moveShip = -4
def rightkeypress():
    global moveShip
    moveShip = 4
def stopShip():
    global moveShip
    moveShip = 0
def start_ending_game():
    global game_ended
    global archy
    game_ended = True
    pygame.mixer.music.stop()
    
    archy.penup()
    archy.home()
    archy.pencolor('white')
    
    archy.write("GAME ENDED",align=('center'), font=("BankGothic", 70,"bold"))
    archy.right(90)
    archy.forward(75)

    
    
    archy.pencolor('green')
    archy.write("Click to exit",align=('center'), font=("Orbitron Regular", 20,"italic"))
    archy.hideturtle()
    
    turtle.exitonclick()

turtle.listen()
turtle.onkey(leftkeypress, 'Left')
turtle.onkey(rightkeypress, 'Right')
turtle.onkey(stopShip, 'Down')
turtle.onkey(start_ending_game, 'Escape')
turtle.onkey(shoot_bullet, 'space')


def spawnEnemies():
    global enemy_list
    for i in range(1,enems+1):
        e = turtle.Turtle()
        e.hideturtle()
        e.shape('assets/enemy.gif')
        e.penup()
        e.goto(random.randint(-300, 300), 800*i)
        e.speed(5)
        e.showturtle()

        enemy_list.append(e)
    return enemy_list
        
def disbetwcors(x1, x2):
    if x1 >= x2:
        return abs(x1-x2)
    elif x2 >= x1:
        return abs(x1-x2)

def no_of_explosions(num_enemies):
    count = []
    for _ in range(num_enemies):
        count.append(0)
    return count
    
#registering the shape of the spaceship, bullet and enemies
turtle.register_shape('assets/ship.gif')
turtle.register_shape('assets/bullet.gif')
turtle.register_shape('assets/enemy.gif')
turtle.register_shape('assets/explosion.gif')
turtle.register_shape('assets/small_enemy.gif')

# creating a turtle for the spaceship
spship = turtle.Turtle()
spship.shape('assets/ship.gif')

# creating a turtle for the enemy counter
small_enemy = turtle.Turtle()
small_enemy.shape('assets/small_enemy.gif')
small_enemy.penup()
small_enemy.hideturtle()

# creating a turtle for the bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape('assets/bullet.gif')
bullet.penup()

# setting the start point
spship.penup()
spship.speed(0)
spship.goto(0, -200)

moveShip = 0
enemies = spawnEnemies()
pygame.mixer.music.load('assets/spship_ambience.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

score = 0
archy.hideturtle()
archy.penup()
archy.goto(375,250)
archy.pencolor('yellow')
archy.write(f"Score: {score}",align=('right'), font=("BankGothic", 20,"italic"))


elienems = 0
archybro.write(f"{elienems}",align=('right'), font=("BankGothic", 15,"italic"))

small_enemy.goto(285,225)
small_enemy.stamp()

explosion_count = no_of_explosions(len(enemies))

totenems = 0

try:
    # adding a game-loop
    while game_over is False:
        enemy_index = 0
        
        
        if totenems == enems:
            game_over = True
            
        if game_ended is True or game_over is True:
            break
        else:
            pass

        
        spship.forward(moveShip)
       

        if bullet.isvisible():
            bullet.setheading(90)
            bullet.forward(25)
            
        if bullet.ycor() > (win.window_height()/2):
            bullet.hideturtle()

        for enemy in enemy_list:
            if (enemy.ycor()) > -300:
                enemy.setheading(270)
                enemy.forward(3)           
                
            elif (enemy.ycor()) <= -300 and enemy.isvisible():
                enemy.hideturtle()
                enemy.home()
                score -= 5
                archy.clear()
                archy.write(f"Score: {score}",align=('right'), font=("BankGothic", 20,"italic"))
                totenems += 1
                break
            
                
            if bullet.isvisible() and enemy.isvisible() and (disbetwcors(enemy.xcor(), bullet.xcor()) < 35) and (disbetwcors(enemy.ycor(), bullet.ycor()) < 33):
                enemy.shape('assets/explosion.gif')
                bullet.hideturtle()
                explosion = pygame.mixer.Sound('assets/explosion.wav')
                explosion.set_volume(0.6)
                explosion.play()
                explosion_count[enemy_index] = 1
                score += 5
                archy.clear()
                archy.write(f"Score: {score}",align=('right'), font=("BankGothic", 20,"italic"))
                elienems += 1
                archybro.clear()
                archybro.write(f"{elienems}",align=('right'), font=("BankGothic", 15,"italic"))
                totenems += 1
        

            if explosion_count[enemy_index] >= 1:
                explosion_count[enemy_index] = explosion_count[enemy_index] + 1
            
            if explosion_count[enemy_index] > 9:
                enemy.hideturtle()
                enemy.home()     
            
            enemy_index = enemy_index + 1 
        
        if spship.xcor() > 330 or spship.xcor() < -330:
            moveShip = 0

        win.update()
        time.sleep(0.017)

    # finishing the code

    game_isover()
    

except turtle.Terminator and _tkinter.TclError and TypeError:
    pass

pygame.mixer.music.stop()

print('\nThanks for playing!')
sys.exit()

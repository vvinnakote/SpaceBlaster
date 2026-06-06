# importing the modules
import turtle, time, pygame, random, sys, _tkinter
import curved_paths  # NEW: load our curved_paths.py file which has polynomial path functions

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

# NEW: Ask the player which enemy path to use
try:
    path_choice = int(win.numinput(
        'Choose Enemy Path',
        '1 = Straight Down\n'
        '2 = Curves\n'
        '3 = S-Curve\n'
        '4 = Swoop\n'
        '5 = Zigzag\n'
        '6 = Mix All!\n\n'
        'Pick a path (1-6)',
        minval=1, maxval=6))
    # STEP 1 of 3: Player picked a number (1-6), now we look up which polynomial
    # functions go with that number (from path_choices dict in curved_paths.py)
    # and set curved_paths.paths to that list
    curved_paths.paths = curved_paths.path_choices[path_choice]  # NEW: update the paths list based on player's choice
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


# NEW: These 3 lists store info about each enemy's curved path
enemy_start_x = []    # NEW: remembers where each enemy started on the x-axis
enemy_start_y = []    # NEW: remembers where each enemy started on the y-axis
enemy_path = []       # NEW: which polynomial function each enemy follows

def spawnEnemies():
    global enemy_list
    for i in range(1,enems+1):
        e = turtle.Turtle()
        e.hideturtle()
        e.shape('assets/enemy.gif')
        e.penup()
        start_x = random.randint(-300, 300)  # NEW: save the random x into a variable so we can remember it
        start_y = 800*i                      # NEW: save the y into a variable so we can remember it
        e.goto(start_x, start_y)             # CHANGED: use our saved variables instead of inline values
        e.speed(5)
        e.showturtle()

        enemy_list.append(e)
        enemy_start_x.append(start_x)   # NEW: remember this enemy's starting x position
        enemy_start_y.append(start_y)    # NEW: remember this enemy's starting y position
        # STEP 2 of 3: Each enemy randomly picks one path function from the list
        # we set in Step 1 (e.g. if player chose 3, this picks from [s_curve])
        enemy_path.append(random.choice(curved_paths.paths))  # NEW: pick a random path from curved_paths.py
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
                # Move enemy down
                enemy.setheading(270)
                enemy.forward(3)

                # --- NEW: CURVED PATH (using polynomials!) ---
                screen_top = 300                                   # NEW: top of the visible screen
                screen_bottom = -300                               # NEW: bottom of the visible screen
                visible_distance = screen_top - screen_bottom      # NEW: 600 pixels of visible area
                if enemy.ycor() <= screen_top:                     # NEW: only start curving once enemy enters the screen
                    t = (screen_top - enemy.ycor()) / visible_distance  # NEW: t = 0.0 at top of screen, 1.0 at bottom
                    t = max(0.0, min(1.0, t))                      # NEW: clamp t so it stays between 0 and 1
                    # STEP 3 of 3: Call the polynomial function that was picked in Step 2
                    # e.g. if enemy got s_curve, this calls: 800 * t³ - 600 * t²
                    x_offset = enemy_path[enemy_index](t)          # NEW: call the polynomial function! returns how far to shift sideways
                    new_x = enemy_start_x[enemy_index] + x_offset  # NEW: new x = starting x + the curve offset
                    new_x = max(-380, min(380, new_x))             # NEW: keep enemy inside the screen boundaries
                    enemy.setx(new_x)                              # NEW: actually move the enemy to the curved x position

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

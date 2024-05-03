[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14694739&assignment_repo_type=AssignmentRepo)

#  Binghamton Assassins 
## CS110 Final Project   Spring, 2024 

## Team Members

 n/a 
 
***

## Project Description

Modeled loosely after the popular high school game Assassins, except playing against the computer. Player gets three tries to shoot the computer while also being shot at. Goal is to kill the computer in the number of bullets given and also to not get killed. 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

The controller initializes the game, and orchestrates main loop. The player character is controlled by player input, includes movement and shooting. The enemy is controlled within the main loop, includes movement and shooting. The bullet object is responsible for collision detection. 

### Features

1. start menu
2. moveable character
3. level up after winning
4. shooting enemies
5. dodging bullets

### Classes

class Player:
    
    def __init__(self, screen, x, y, img_file):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_file = img_file
        self.img = pygame.image.load(img_file)
        self.bullets = 4
    def move_right(self):
        """
        moves position right by 1
        args: None
        return: None
        """
        self.x+=2
    def move_left(self):
        """
        moves position left by 1
        args: None
        return: None
        """
    def shoot(self, enemy):
        self.bullets -= 1
        if(self.bullets <= 0):
            exit()
        bullet = Bullet("./assets/bullet.png", self.screen, True, self.x + 124, self.y+50, enemy)
        bullet.move()
        """
        creates bullet object
        args: None
        return: Bullet
        """
    
    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
        
class Enemy:
    def __init__(self, screen, x, y, img_file):
        """initalizes enemy obj

        Args:
            screen (pygsme.Surface): surface where enemy is drawn
            x (int): initial x coordinate of enemy
            y (int): initial y coordinate of enemy
            img_file (str): file path enemy sprite
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.img_file = img_file
        self.img = pygame.image.load(img_file)
        self.amountMove = 5
        self.left = False
    def move_right(self):
        """
        moves pos right by 2
        args: None
        return: None
        """
        self.x+=2
    def move_left(self):
        """
        moves position left by 2
        args: None
        return: None
        """
        self.x-=2
    def move(self, enemy):
        """moves enemy horizontally, shoots random bullets

        Args:
            enemy: target enemy obj
            
        Returns:
            None
        """
        if(random.randint(1, 75) == 1):
            self.shoot(enemy)
        if(self.amountMove > 0):
            self.amountMove -= 1
            if(self.left):
                self.move_left()
            else: 
                self.move_right()
        else: 
            self.amountMove = random.randrange(5, 10)
            self.left = True if random.randint(0, 1) == 1 else False
    def shoot(self, enemy):
        bullet = Bullet("./assets/bad_bullet.png", self.screen, False, self.x + 150, self.y+200, enemy)
        bullet.move()
        """
        creates a bullet object, enables it to move
        args: ebnemt: target enemy obj
        return: 
        """
    def draw(self):
        """
        draw enemy sprite on screen
        Args:
            none
        Returns: 
            None
        """
        self.screen.blit(self.img, (self.x, self.y))

class Bullet:
    def __init__(self, img_link, screen, good, x, y, sprite):
        """initializes bullet obj

        Args:
            img_link (str): image file for the bullet
            link (_type_): _description_
            screen: screen object that bullet is drawn
            good (bool): bullet is enemy/player's 
            x (int): x coordinate of bullet
            y (int): y coordinate of bullet
            sprite: bullet's target
        Returns: 
            None
        """
        self.screen = screen
        self.good = good
        self.x = x
        self.y = y
        self.img_link = img_link
        self.img = pygame.image.load(img_link)
        self.sprite = sprite
    def move(self):
        """updates pos of bullet, checks for collisions with the target sprite. program exits when that occurs
        Args:
            None
        Returns:
            None
        """
        while(self.y > 0 if self.good else self.y < 607):
            self.y = self.y - 1 if self.good else self.y + 1
            self.screen.blit(self.img, (self.x, self.y))
            pygame.display.flip()
        if(self.good):
            if(abs((self.sprite.x + 150)-self.x) < 10):
                exit()
            else: 
                if(abs((self.sprite.x + 124)-self.x)< 10):
                    exit()
    
class Controller:
    def __init__(self, image_file):
        """initializes controller object

        Args:
            image_file (str): file path for game bg
            
        Returns:
            None 
        """
        pygame.init()
        self.image_file = image_file
    
    def mainloop(self):
        """
        Controlls game flow
        Args: 
            None
        Returns: 
            None
        """
        screen = pygame.display.set_mode((1080, 607))
        background = pygame.image.load(self.image_file)
        
        player = Player(screen, 390, 400,"./assets/player.webp")
        enemy = Enemy(screen, 390, 0, "./assets/enemy/png")
        while(True):
            screen.blit(background, (0, 0))
            player.draw()
            enemy.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            pressed = pygame.key.get_pressed()
            if(pressed[pygame.K_LEFT]):
                player.move_left()
            if(pressed[pygame.K_RIGHT]):
                player.move_right()
            if(pressed[pygame.K_SPACE]):
                player.shoot(enemy)
            enemy.move(player)
            pygame.display.flip()

## ATP

| Step | Procedure | Expected Results |
|----------------------|:--------------------:|----------------------------------:|
|  1  Player Movement   |  1. Start game 2. Press left arrow key 3. Verify player moves left 4. Press right arrow key 5. Verify player moves right |Player moves according to keys pressed |
|  2  Enemy  | 1. Start game 2. Observe enemy movement | Enemy moves randomly on screen |
|  3  Collision Detection  | 1. Start game 2. Shoot at enemy 3. Verify bullet hits enemy 4. Shoot but miss at enemy 5. Verify bullet did not hit enemy | Bullet hits enemy when it is supposed to, bullet disappears after collison |
|  4  Game over  condition | 1. Start game 2. Lose as a player 3. Verify game over screen appears | game over is displayed when player loses all lives or enemy is hit | Start game over | Win (hit enemy) | verify game over screen appears |
|  5  Menu | 1. Start game 2. Select options, start, quit 3. verify correct actions occur depending on what is pressed | verify all actions work as intended |

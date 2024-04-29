[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14694739&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Binghamton Assassins 
## CS110 Final Project   Spring, 2024 

## Team Members

 n/a 
***

## Project Description

Will be like the popular high school game Assassins, except playing against the computer. You will get three tries to shoot the computer while also being shot at. If dead, there is a chance for a revive. Goal is to kill the computer in the number of bullets given and also to not get killed. 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. start menu
2. moveable character
3. level up after winning
4. interactive objects
5. revive feature

### Classes

class Player:
    def __init__(self):
        """
        Initialzes player object
        Args: None
        Returns: None
        """
    def shoot(self):
        """
        actual shooting motion from the player to computer 
        Args: None
        Returns: None
        """
    def revive(self):
        """
        shows a revive question for player to answer
        Args: None
        Returns: None
        """
class ComputerPlayer:
    def __init__(self):
        """
        Initializes comp (player 2) object
        Args: None
        REturns: None
        """
    def shoot(self):
        """
        shooting motion from computer to player
        Args: None
        Returns: None
        """
class Game:
    def __init__(self):
        """
        Initializes game object
        Args: None
        Returns: None
        """
    def start_menu(self):
        """
        The start menu shows up (shows a start button with instructions and explanation, possibly what level you are currently on)
        Args: None
        Returns: None
        """
    def level_up(self):
        """
        Game gets more difficult if you win
        Args: None
        Returns: None
        """


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...

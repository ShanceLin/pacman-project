# Cover Page
## CS 110 Final Project, Fall Semester, 2018
### [Github URL]
### [Project Demo Presentation as Google Slide URL]
***
## Team: Foreman
#### Nick, Rachael, Shance

***

## Project Description
Redesigned version of the classic pacman game featuring beloved computer science teacher, Dennis Foreman, as the packman, and <whoever the ghose is> as the ghost. pacman is a game in which the pacman's goal is to eat all of its food pellets without being touched by the ghosts, each pellet adds to the pacman's score. If the pacman eats a power pellet, it then has the ability to eat the ghost, giving it more points.
***    

## User Interface Design
* Main menu/ Start Screen
    * This screen is the first thing that the user sees, displaying the name "Pacman" and allowing the play to press the "start game" button, or "quit" button. Click "instructions" to learn how the game is played
* Instructions Screen
    * The screen tells the user how to play and the controls for the game. From here the user can press "back" to return to the main menu
* The Game Menu
    * Screen where the actual game of pacman takes place, using the arrow keys you can move the packman around and play the game like it tells you in the instructions screen. Once all the pellets are eaten the game will proceed to the next level, and the score will continue to increase. The game is "over" when the pacman loses all three of its lives, which happens when the ghosts touch it.
* Game Over Menu
    * This screen appears when pacman loses all of its three lives, and displays the message "GAME OVER" and gives the option to click "play again" or "quit"
<paste each screen menu here>
***        

## Program Design
* Additional Libraries Used:
    * Pygame:
        * https://www.pygame.org/
        * A cross platform set of Python modules designed for writing video games, developed by Pete Shinners and the Pygame community. includes crucial graphical elements as well as musical playback functionality
* Class and File relationships
    * <insert flow chart here>
* List of classes
    * **Pacman**: A class that defines the pacman, which takes the form of the beloved computer science teacher, Dennis Foreman. The class sets up the speed, lives, and controls for moving the pacman.
    * **Pellets**: A class that defines the pellets pacman eats to increase the game score. Sets the coordinate each pellet is generated to
    * **BigPellets**: A class that defines the power pellets pacman eats so he can kill the enemies, eating these increases his score more than the regular pellets do. Also changes the pacman image from Dennis to the terminator. Sets the coordinate each pellet is generated to
    * **Layout**:
    * **Ghost**: A class that defines pacman's enemies, which take the form of <name of ghost> .
***

## Tasks and Responsibilities
* Software Lead - Rachael
    * Arranged group meetings to make sure the front and back end specialist were both on the same page and working on their code in a timely fashion. Also wrote up the ATP, README, and presentation slides.
* Front End Specialist - Nick
    * Front-end lead conducted research on using pygame to create visual aspects such as buttons and on-screen text. He used this information to design and program a consistent UI to help the player navigate the title screen, the instructions page, and the “GAME OVER” screen. In addition to implementing the wide majority of the visual element for the UI, he also collaborated with the backend to index into images and change them with certain parts of the gameplay
* Back End Specialist - Shance
    * The back end specialist helped with the “Model” portion of pacman by writing all of the major classes that would be used in the main game, as well as implementing major pygame functionality into each of them. He also made headway in major game mechanics such as the basic pacman movement and advanced functionality such as the pacman having wall boundaries. He collaborated with the Front End Specialist in the implementation of the classes into our Controller file, as well as develop the ability to have and increase the players score.
***

## Testing
* Menu Testing
    * First we run python3 main.py and check that all of GUIs on our main screen work. Like being able to go to the instructions screen and then back to the main. Then we run the game and lose on purpose to make sure that the end game window pops up. Then we play again, pressing the "play again" button on the game over menu and win on purpose to make sure the level changes. We make sure that the quit buttons on every window work properly
* Game Testing
    * We run the game testing out the controls making the pacman move around using the up, down, left, right arrow keys. Then we make the pacman run into a wall to make sure the boundaries are working properly. Then we test the gameplay, making the pacman eat pellets seeing that the score increases, then we eat a power pellet to make sure pacman changes images and is able to now eat the ghost (also increasing its score by more points).

* A copy of your ATP

| Step | Procedure | Expected Results | Actual Results | Al |
| --- | --- | --- | --- | --- |
| 1 | Run main.py | Gui window appears with the game displayed with pacman, his food pellets, and ghosts. also has score in the top left corner. the ghosts move around randomly, the pellets stay in place, and pacman is moved manually |   |   |
| 2 | Pressing the up arrow | Pacman character moves up |   |   |
| 3 | Pressing the down arrow | Pacman character moves down |   |   |
| 4 | Pressing the left arrow | Pacman character moves left |   |   |
| 5 | Pressing the right arrow | Pacman character moves right |   |   |
| 6 | Pacman touches little pellet | The pellet disappears (because pacman “ate” it) and the score increases by 1 |   |   |
| 7 | Pacman touches big power pellet | The pellet disappears (because pacman “ate” it) and the score increases by 10, also pacman changes color |   |   |
| 8 | Pacman touches ghost | Pacman “dies” and the game ends. “Game Over” is displayed |   |   |
| 9 | Pacman touches ghost while on power pellet | Ghost disappears because he “dies” and the score increases by 50 |   |   |
| 10 | Pacman touches wall | He is unable to pass the wall because it is a boundary |   |   |
| 11 | Pacman eats all the pellets | “You win! Next level” prints and the level of the game changes, re-generating the pellets and ghosts |   |   |

# Requiremets specification
## Purpose of the application
The app I'll be developing on the course is a simple platformer game. I will develop the game in python with the pygame library.

The idea is for the game to be composed of small levels that the player has to pass in order to progress to next levels. In addition to the game itself, the app will also include some menu windows to have a basic UI.


## UI draft
Here's my idea of what components and functionality the UI of the game ought to have (at least):

![ui-draft](./images/ui-draft.png)
#### Start window
When first starting the game, the player gets to a start window. Here the player can select to begin a new game. An interesting feature would be to also offer a chance to continue a previous game if one exists.

#### Game window
The game window hosts the game itself. Here the player either maneuvers through the level or falls to hers / his demise.

#### Post-game window
After either dying / finishing the game, the player sees the post-game window. The main function of this window is to give the player a chance to either quit or retry. Some stats could be displayed here too, a highscore for example.


## The base functionality of the application
### The UI
- The most important features from the UI draft above
  - [x] The player can start the game with a new game button in the Start window
  - [x] The post-game window pops up when the player dies or wins
    - [x] A choice to retry or quit (the game doesn't just close when the main game loop finishes)
    - [x] The highscore is displayed

### The Game
- Game levels
  - [x] The game should have at least 2 levels
  - [x] The levels can be passed
  - [x] Once a level is passed, the player advances to the next level
- [x] Player physics and movement
  - [x] Player can move in the game and collide with the game map
  - [x] Player can jump and fall
- A system for scoring game runs
  - [x] highscore based on number of levels passed
  - For example based on collectibles or playthrough time

### Storing data
- [x] Game results are stored in a database
  - [x] The highscore is conserved even if the game is quit
  - [x] Also the number of runs

## Additional ideas for features
### The UI
- A settings window
  - For example to set the resolution
- A level browser
  - If more levels are implemented, a window for choosing them would be nice
- [x] A stats window
  - To show database contents
- [x] A controls window
  - To show game controls

### The game
- Game levels
  - More levels
  - Enemies
  - Moving map features
- Player physics and movement
  - Physics could be altered on different levels

### Storing data
- The level to which the player has progressed is saved
  - The game can be continued from the same point where left off
  - Needs more levels to be an useful feature




# Changelog
## Week 3
### Project structure
- Structured the code based on the course's [example game](https://github.com/ohjelmistotekniikka-hy/pygame-sokoban)

### Gameplay
- The game loop works and the game is rendered to the player
- Added 1 playable level
- Added physics
  - Player can fall
  - Player can collide with the map from any direction
- Added player-controlled movement
  - Player can move left and right
  - Player can jump

### Tests
- Tested that the player can move left and right

## Week 4
### Technicalities
- All rendering refactored into its own Renderer class
  - For scaling and rendering content to the display
- Player movement refactored
  - split into many smaller methods
- Pylint and autopep added
  - With respective tasks
- Test coverage rising
  - Added tests for player movement

### Features visible to user
- Started implementing UI
  - Added a Button class to implement buttons with different on-click functions
  - Added a menu class mainly to host buttons
  - Added a MenuLoop class to loop the menu
    - Currently very similar to the GameLoop class

### Gameplay
- The player can now die by falling
  - Currently this just throws the player back to the start menu

## Week 5
### Technicalities
- Refactor GameLoop
  - Instead of a single level, takes a list of levels as a parameter
  - Save game results into database
- Completely refactor UI
  - A single MenuLoop hosts, displays and updates a list of menus instead of a single menu
- A DataBase class added
  - game results are stored here
- A config file added
  - Currently display height can be set here
  - Support dotenv in the future
- Added and updated tests

### Features visible to user
- Level completion works
  - Player can progress from level to level
  - 2 new levels added
- A working UI
  - Added multiple different menus
  - Navigation between menus works with buttons
  - Game result affects menu state
  - Menus can display data from database
  - Moved to using native resolution for menus
    - No more scaled and pixelated menus
- Everything in the game and in menus should scale to any display size

### Gameplay
- Progress to the next level by reaching the flag on each level

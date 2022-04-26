# Architecture description
*This represents the current state of the program and is most likely subject to changes*

## The most important classes and their relationships in a class diagram
This diagram is not exhaustive - instead of depicting every single method and dependency, it focuses on providing an understandable overview
```mermaid
classDiagram
  class Player{
    movement()
    controls()
  }
  class Level{
    player
    other sprites
  }
  class Renderer{
    content
    scale()
  }
  class GameLoop{
    levels
    renderer
    handle_events()
  }
  class Button{
    on_click()
  }
  class Menu{
    buttons
  }
  class MenuLoop{
    menus
    handle_events()
    update_menus()
  }
  class DataBase{
    store()
    query()
  }
  
  
  
  Player "1"-- Level
  Renderer ..> Level
  GameLoop --"*" Level
  GameLoop --"1" Renderer
  GameLoop -- DataBase
  Menu --"*" Button
  MenuLoop --"*" Menu
  MenuLoop -- DataBase
  
```
### Some notes on the classes
The loop classes (**GameLoop** , **MenuLoop**)
  - A GameLoop takes a list of levels, a renderer, a clock and a database
    - The loop checks for events, updates the level and stores game result using the database
  - A MenuLoop takes a dict of menus and a database
    - The loop checks for clicks on buttons, handles navigation between menus, updates the menus and queries the database to display its contents

The **DataBase** class
- Every time a game loop ends, the level to which the player got to gets saved
- The database can be queried for the total amount of tries and the highscore (highest level passed)

The **Level**  class
  - A level has a player and other sprites such as map tiles

The **Menu**  class
  - The most important functionality of a menu is to host **buttons** 

The **Button** class 
  - A button consists of text, a rect and a reference to a function
  - When the user clicks the button the function gets executed
  - Any function can be assigned: for example starting a new game, giving an exit call or providing a dict key to navigate to a new menu window are all implemented as on_click functions

The **Renderer** class
  - A renderer takes a level as content to render
  - A renderer renders the content to the display and scales it from a small drawing surface to the full-sized display
    - This makes the pixelated look of the game happen
    - Menus do not have a separate renderer as native resolution is used in the UI

What's a **Sprite** and what's not
  - All in-game stuff is sprites
    - Makes especially the drawing to the screen part easier
  - UI does not utilize sprites
    - Writing text on sprites gets unecessarily complex fast
    - Scaling sprites with text easily leads to unwanted pixelation
    - Using native resolution rects and text instead looks nicer and is easier to scale to any display size

## Sequence diagrams
### Starting the program and starting a new game
```mermaid
sequenceDiagram
  actor User
  
  User->>MenuLoop: invoke start
  activate MenuLoop
  MenuLoop->>menu: Get current menu (start menu)
  menu->>buttons: Get the menu's buttons
  buttons-->>menu: on_click functions
  menu-->>MenuLoop: Display current menu content and provide on_click functions
  
  User->>MenuLoop: Click start
  MenuLoop->>buttons: Execute start button's on_click function (start_game())
  deactivate MenuLoop
  buttons-->>User: Start the game loop for the user 
```

# User manual
## Requirements
- Poetry for installing dependencies
- Python >= 3.8

## Installation
Once you have the requirements setup you can download the source code for the latest [release](https://github.com/eemilhaa/ot-harjoitustyo/releases/).

Download the dependencies with:
```console
poetry install
```
(Make sure to run this and all CLI commands in the root of the repository)

## Configuration
Configuration is done in the [.env](../.env) file found in the root of the repository. In this file you can input your desired display height and the filename for the database file that stores your game data. The format of the file is the following:
```
DISPLAY_HEIGHT=900
DATABASE_FILENAME=database.db
```
`DISPLAY_HEIGHT` is the height of the game window in pixels and `DATABASE_FILENAME` is the name for the database file.

## Starting the program
After you have the dependencies (and possibly customized the configuration file) you can start the program with:
```console
poetry run invoke start
```
For a listing of all the available CLI commands refer to the [readme](https://github.com/eemilhaa/ot-harjoitustyo/blob/main/README.md#available-cli-commands)

## Navigating the menus
The program starts from a start menu. You can navigate between menus by clicking the buttons. Click the **CONTROLS** button to see the controls for playing the game. For an in-depth look at the menu structure see the [UI section](https://github.com/eemilhaa/ot-harjoitustyo/blob/main/documentation/requirements-specification.md#ui) of the requirements specification document.

## Starting a new game
Starting a new game is as simple as pressing the **START** button.

## Gameplay
The idea of the game is to jump through the level without falling down. You can progress in the game by reaching the flag on each level. Control your character with the left and right arrow keys and space.

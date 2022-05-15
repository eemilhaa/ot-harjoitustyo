# Test documentation
The game has unit tests as well as integration tests. The testing is focused on the applicatiopn logic, and the code related to the UI is left untested.

## Unit and integration tests
### The game logic
The game logic is found in the [**Player**](../src/game/sprites/player.py), [**Level**](../src/game/level.py) and [**GameLoop**](../src/game/game_loop.py) classes. The Player class is tested with the [**TestPlayer**](../src/tests/player_test.py) test class, testing the player's methods one by one. Testing player controls is done by feeding the desired pygame event objects into the player controls.

The GameLoop tests focus on the integration between the game component classes. Testing the GameLoop "as is" would be quite difficult, so the [**TestGameLoop**](../src/tests/game_loop_test.py) test class is implemented by injecting Stub versions of some dependencies that would make testing tricky. 

### Storing and querying data
The [**DataBase**](../src/database.py) class is responsible for all data storing and querying. It is tested with the [**TestDataBase**](../src/tests/database_test.py) class. The database tests use a separate database set in the .env.test file in order to not interfere with the users actual game data.

### Loading files
The loaders package is responsible for loading all the files the game needs (images, fonts). The package is tested with the [**TestLoaders**](../src/tests/loader_test.py) test class.

## Test coverage
TODO

## System testing
The complete program "as the user would use it" has been tested manually and should comply with the requirements specifications.

### Installation and configuration
Installation has been tested manually using the instructions found in the [user manual](./user-manual.md). Configuring the program with the [.env](../.env) file has been tested as well.

### Features
The game has been tested to fulfill all features specified in [requirements specification](./requirements-specification.md).

### Operating systems
The game has been tested on both Linux and macOS.

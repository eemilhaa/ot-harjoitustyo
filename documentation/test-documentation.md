# Test documentation
The game has unit tests as well as integration tests. The testing is focused on the applicatiopn logic, and the code related to the UI is left untested.

## Unit and integration tests
### The game logic
The game logic is found in the **Player**, **Level** and **GameLoop** classes. The player class is tested with the TestPlayer test class, testing the player's methods one by one. Testing player controls is done by feeding the desired pygame event objects into the player controls.

The GameLoop tests focus on the integration between the game component classes. Testing the GameLoop "as is" would be quite difficult, so the TestGameLoop test class is implemented by injecting Stub versions of some dependencies that would make testing tricky. 

### Storing and querying data
The DataBase class is responsible for all data storing and querying. It is tested with the TestDataBase class. The database tests use a separate database set in the .env.test file in order to not interfere with the users actual game data.

### Loading files
The loaders package is responsible for loading all the files the game needs (images, fonts). The package is tested with the TestLoaders test class.

## Test coverage
TODO

## System testing
The complete program "as the user would use it" has been tested manually and should comply with the requirements specifications.

### Installation and setup
TODO

### Operating systems
The game has been tested on both Linux and macOS.

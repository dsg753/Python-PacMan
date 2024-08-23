# Pac-Man Game in Pygame
This repository contains a simple implementation of the classic Pac-Man game using Python and Pygame. The project demonstrates basic game development concepts, including player movement, collision detection, AI for enemies, and basic sound integration.

# Introduction
This project is a simplified version of the classic Pac-Man game. The player controls Pac-Man, navigating through a maze while eating pellets and avoiding ghosts. The game ends if Pac-Man is caught by a ghost or if all the pellets are consumed.

# Features
- **Pac-Man Movement**: Use the arrow keys to move Pac-Man around the maze.
- **Ghost AI**: Ghosts move randomly within the maze, changing direction when they hit walls.
- **Pellets**: Collect all the pellets to win the game.
- **Collision Detection**: Includes basic collision detection between Pac-Man, ghosts, walls, and pellets.
- **Sound Effects**: Plays sound effects when Pac-Man eats a pellet or collides with a ghost.

## Installation
**Install the required packages**:
   Ensure you have Python and Pygame installed. If not, you can install them using:
   ```sh
   pip install pygame
   ```

 **Run the game**:
   ```sh
   python pacman.py
   ```
## How to Play
- **Start the Game**: Run the `pacman.py` file.
- **Move Pac-Man**: Use the arrow keys to move Pac-Man in the desired direction.
- **Objective**: Collect all the pellets while avoiding the ghosts.
- **Game Over**: The game ends if a ghost catches Pac-Man, or you win if you collect all the pellets.

## Code Explanation
The code is structured to handle different aspects of the game, including player movement, ghost AI, collision detection, and rendering.

### Main Components
- **Constants and Colors**: Basic constants for game dimensions, speeds, and colors are defined at the beginning of the code.
- **Initialization**: Pygame is initialized, and the game window is set up.
- **Game Elements**:
  - **Walls**: Defined using rectangles (`pygame.Rect`) and drawn as blue blocks.
  - **Pellets**: Small white circles scattered throughout the maze for Pac-Man to collect.
  - **Ghosts**: Red circles that move randomly within the maze. Ghosts change direction upon hitting a wall.
  - **Pac-Man**: Controlled by the player, represented by a yellow circle.
- **Game Loop**: The main game loop handles events (like key presses), updates positions of Pac-Man and ghosts, checks for collisions, and redraws the game elements on the screen.
- **Collision Detection**:
  - **Pac-Man with Walls**: Prevents Pac-Man from moving through walls.
  - **Ghosts with Walls**: Adjusts ghost direction when they hit a wall.
  - **Pac-Man with Ghosts**: Ends the game if Pac-Man collides with a ghost.
  - **Pac-Man with Pellets**: Removes pellets from the game when Pac-Man eats them, playing a sound effect.
### Sound Effects

Two sound effects are included:
- **Eating Pellet**: Played whenever Pac-Man eats a pellet.
- **Pac-Man Death**: Played when Pac-Man collides with a ghost.

### Game Over Conditions
- **Victory**: The player wins by collecting all pellets.
- **Defeat**: The game ends if Pac-Man collides with a ghost.

## Known Issues
- **Ghost AI**: The ghosts move randomly and may sometimes seem to wander without posing much of a threat. They do not currently follow Pac-Man as they do in the original game.
- **Wall Collision**: In certain corner cases, Pac-Man may "stick" to a wall if the movement direction is changed too quickly.
- **Ghost Spawn Locations**: Ghosts are spawned randomly in areas outside of walls, but occasionally they might spawn very close to walls, leading to immediate direction changes that look unnatural.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

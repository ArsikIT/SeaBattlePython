# Sea Battle Game

This is a graphical implementation of the classic *Battleship* game using Python's Tkinter library. The game allows two players to battle against each other by placing ships on a grid and guessing the positions of the opponent's ships. The game also supports playing against the computer, where the computer will make random guesses.

## Features

- **Human vs Human**: Two players can take turns attacking each other's ships on separate grids.
- **Human vs Computer**: One player can compete against the computer, which makes random guesses.
- **Grid-based Game Field**: The game is played on a grid of 8x8, where players can place their ships horizontally or vertically.
- **Interactive GUI**: Players interact with the game through clicks on the grid. Left-click to miss a shot, right-click to hit a ship.
- **Game Restart**: You can restart the game at any time to play again with a fresh setup.

## Game Setup

- The game consists of two grids, one for each player. Each player places a set of ships on their grid.
- Players take turns attacking their opponent's grid. If a ship is hit, the opponent's ship is marked on the grid.
- If all of an opponent's ships are destroyed, the game ends and a winner is declared.

## Game Rules

- The game field is an 8x8 grid.
- Each player has a maximum of 4 ships (ships of different lengths), which they place on their grid at the start of the game.
- Players can attack the opponent's grid by clicking on the cells, and the opponent's ships will be marked when hit.
- The game ends when all of the opponent's ships are sunk.

## How to Play

1. **Human vs Human Mode**:
   - Player 1 and Player 2 will take turns to place ships on their respective grids.
   - Players can click on the grid to attack the opponent's ships.
   - The game continues until all of the opponent's ships are sunk.

2. **Human vs Computer Mode**:
   - Player 1 places ships on their grid.
   - The computer will take its turn by randomly selecting cells on Player 1's grid to attack.
   - The game continues until all of Player 1's ships are sunk or the player wins by sinking all of the computer's ships.

3. **Restart the Game**:
   - You can click the "Restart" button to reset the game and start fresh with new ships.

## Requirements

- Python 3.x
- Tkinter library (comes pre-installed with Python)



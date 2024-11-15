# Quoridor Game

## Introduction
The challenge is to design and implement an AI capable of playing Quoridor, a strategic two-player board game where each player must navigate a pawn across a 9x9 grid, placing walls to hinder the opponent's progress. The objective is to be the first player to move their pawn to the final row of the opponent's side of the board. Players can either move their pawn or place a wall each turn, and the game requires a blend of tactical wall placement and strategic pawn movement.

## Components of the Game

### State Space
The game’s state space is a 9x9 grid, where each player has:
- One pawn, starting at opposite ends of the board.
- 5 walls, which they can place to block the movement of the opposing pawn.

Each game state is represented by the positions of both pawns and the placement of the walls.

### Agents
The game is designed for two agents:
- A human player or an AI agent on each side.

The agents take turns moving their pawns or placing walls.

### Start State
- Player 1's pawn starts on the bottom row (row 1).
- Player 2's pawn starts on the top row (row 9).

### Goal State
The game is won when one player successfully moves their pawn to the opposite side of the board, reaching the last row before their opponent.

### Actions
Each turn, the player must choose between:
- Moving the pawn one square horizontally or vertically (no diagonal moves allowed).
- Placing a wall either horizontally or vertically between two grid squares to block the opponent's pawn movement.

## Game Rules

### Pawn Movement
- Pawns can move one square at a time, either horizontally or vertically.
- When pawns are adjacent, a player can jump over the opponent’s pawn if there’s no wall directly behind it.
- If a wall is blocking the direct jump, the player can move to one of the adjacent open squares.

### Wall Placement
- A player may place a wall between two squares to block the movement of pawns.
- Walls can only be placed vertically or horizontally and must cover two adjacent squares.
- Walls cannot be placed diagonally.
- The game ensures that neither player can fully block the other from reaching their goal, as there must always be at least one path available.

### Additional Feature: Timer
To increase the game's intensity, each player is allocated 10 minutes per turn to make their moves. This time constraint adds a layer of strategic pressure, as players need to think both quickly and efficiently.

## AI Algorithms

### Minimax with Alpha-Beta Pruning
The AI implemented for Quoridor is designed to think both strategically and tactically, ensuring that it can navigate the board efficiently while obstructing the opponent. We incorporated the minimax algorithm with alpha-beta pruning.

#### Minimax Process
- **Maximizing player’s turn**: The AI tries to find the move that gives it the best strategic advantage.
- **Minimizing opponent’s turn**: It assumes the opponent will play optimally and tries to limit the opponent’s progress.

### Alpha-Beta Pruning
This optimization technique is applied to cut off branches in the decision tree that are guaranteed to be irrelevant, allowing the AI to delve deeper into the game without overloading computational resources. It evaluates only the most critical moves.

### Heuristic
The heuristic function calculates a score by taking both pawn distance to goal and the walls into consideration along with mobility of the piece.

## Game Development: Front-End Using Pygame

### Setting Up the Pygame Display
The board consists of a 9x9 grid with alternating brown and orange squares. Each square represents a potential movement position for the pawns, while intersections represent wall placement points. We carefully designed the visual elements of the board to ensure clarity. The pawn positions and wall placement opportunities are easily distinguishable, with walls appearing between squares in a 8x5 grid of intersection points.

### Basic Event Loop
The core of the game’s interaction is handled through an event loop that tracks user inputs (mouse clicks) and updates the game state in real-time.
- **Pawn Movement**: When a player clicks on their pawn, valid movement options are highlighted, allowing the player to see where the pawn can move.
- **Wall Placement**: Hovering over an intersection between squares highlights potential wall placements, and clicking places the wall if the move is valid.

### User Interaction
- **Pawn Interaction**: Players can click on their pawn to highlight all valid movement options. Once a destination square is selected, the pawn moves there.
- **Wall Interaction**: Hovering over an empty space between two squares highlights valid wall placements. A click confirms the placement of the wall, and it is immediately rendered on the board.

## Technical Backend Details

### State Representation
The game state is modeled as a combination of:
- A 9x9 grid representing the positions of the pawns.
- Structures to track the placement of walls, ensuring the rules of wall placement are respected (e.g., no diagonal walls, no complete blockage).
- **Pawn Coordinates**: The position of each pawn is stored as a tuple of (x, y) coordinates on the grid.
- **Wall Representation**: Walls are represented by their positions between grid squares, with checks to ensure walls don’t completely block the opponent’s path.

### AI Optimization
The Minimax algorithm is enhanced with Alpha-Beta Pruning, allowing the AI to calculate deeper, more strategic moves without sacrificing performance. A* ensures the AI takes the shortest path to the goal while adjusting to walls in real-time, and GBFS is used to react quickly when immediate decisions are needed.

## Installation
To get started with the Quoridor Game, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quoridor-game.git
2. Navigate to the project directory:
   ```bash
   cd Quoridor
3. Install the required dependencies:
   ```bash
   npm install
4. Run the game:
   ```bash
   npm start

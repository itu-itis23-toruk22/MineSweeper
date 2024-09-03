# MineSweeper

This project is a Python implementation of the classic Minesweeper game.

## Features

**Customizable Grid Size and Mine Count:**
  -The game allows the player to choose the size of the grid and the number of mines.

**Game States:**
  -The game tracks whether the player wins by successfully clearing the grid or loses by revealing a mine.

## How it Works

1. **Revealing Cells:**
   - The player selects a cell to reveal. If the cell contains a mine, the game is over.
   - If the cell is safe, it reveals a number indicating how many mines are adjacent to that cell.
   - If no adjacent mines are present, the cell is cleared, and surrounding cells are automatically revealed.
  
2. **Winning and Losing:**
   - The player wins by revealing all non-mine cells and correctly flagging all mines.
   - The player loses if they reveal a cell containing a mine.

3. **Replay**
   - Once the game ends, either by winning or losing, the player can start a new game with `r` key

### Credits

- **Minesweeper Icons** by <a href="https://www.flaticon.com/free-icons/mine" title="mine icons"> Mine icons created by Creaticca Creative Agency - Flaticon</a>). Icons used with permission.

### License

This project licensed with MIT license.
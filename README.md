
# Mystery Island Adventure

A Python-based, terminal text adventure in which a shipwrecked survivor must explore a mysterious island, collect essential items, manage limited energy, solve obstacles, and activate a lighthouse beacon to escape.

## Project Overview

Mystery Island Adventure is a command-line game built with Python's standard library.

The player begins stranded on a beach after a terrible storm. To escape, the player must travel through five locations, collect a rope and a lantern, make decisions that affect energy, and restore the lighthouse beacon.

The game has two possible outcomes:

- **Victory:** Successfully activate the lighthouse beacon while having energy remaining.
- **Defeat:** Run out of energy before completing the adventure.

The game also supports replaying with a fresh player state.

## Features

- Interactive terminal menu.
- Five connected island locations.
- Player name and game-state tracking.
- Inventory management.
- Collectible rope and lantern.
- Location-specific puzzles and requirements.
- Energy management and meaningful decisions.
- Victory, defeat, and quit conditions.
- Replay functionality.
- Input validation for unexpected menu choices.
- Automated unit tests using Python's `unittest`.

## Technologies

- Python 3
- Python standard library
- `unittest` for automated testing
- Git and GitHub for version control

No third-party Python packages are required.

## Project Structure

```text
mystery-island-adventure/
├── main.py
├── game.py
├── tests/
│   ├── test_game.py
│   └── test_main.py
├── README.md
├── GAME_DESIGN_DOCUMENT.md
└── .gitignore
```

### Main files

| File | Responsibility |
|---|---|
| `main.py` | Terminal interaction, menus, player input, replay, and application flow |
| `game.py` | Game state, movement rules, inventory, energy, and victory conditions |
| `tests/test_game.py` | Tests for game logic and rules |
| `tests/test_main.py` | Tests for application flow and replay |
| `GAME_DESIGN_DOCUMENT.md` | Game concept, requirements, mechanics, and design decisions |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Aocheg/mystery-island-adventure.git
```

### 2. Enter the project directory

```bash
cd mystery-island-adventure
```

### 3. Check your Python installation

```bash
python3 --version
```

Python 3 is required.

### 4. Run the game

```bash
python3 main.py
```

The game starts in your terminal. Enter your name and follow the displayed menu options.

## How to Play

### Objective

Reach the Lighthouse, use the lantern to activate its beacon, and signal a rescue boat before your energy runs out.

### Island map

```text
Beach
  |
  v
Jungle
  |
  v
Cave
  |
  v
Old Bridge
  |
  v
Lighthouse
```

The player progresses forward through the island.

### Important items

| Item | Found at | Purpose |
|---|---|---|
| Rope | Jungle | Required to leave the Jungle and cross the Old Bridge |
| Lantern | Cave | Required to leave the Cave and activate the Lighthouse beacon |

Items are not consumed when used.

### Energy system

The player starts with 5 energy points.

| Action | Energy cost |
|---|---:|
| Beach to Jungle | 1 |
| Safe Jungle route to Cave | 1 |
| Dangerous Jungle shortcut to Cave | 2 |
| Careful Cave search | 0 extra |
| Rushed Cave search | 1 extra |
| Cave to Old Bridge | 1 |
| Careful bridge crossing | 1 |
| Rushed bridge crossing | 2 |
| Collecting the Rope | 0 |
| Checking inventory or status | 0 |
| Invalid or unavailable action | 0 |
| Activating the beacon | 0 |

Energy cannot fall below zero. If a valid action uses the player's final energy point, the adventure ends in defeat.

An action that costs more energy than the player currently has cannot be completed.

### Menu controls

At ordinary locations:

1. Explore
2. Check surroundings
3. Collect item
4. Check inventory
5. Check status
6. Quit

At the Lighthouse:

1. Explore
2. Check surroundings
3. Collect item
4. Check inventory
5. Activate lighthouse beacon
6. Check status
7. Quit

The game also asks for a decision when the player reaches the Jungle route, searches the Cave, or crosses the Old Bridge.

### Winning strategy

A minimum-cost winning route is:

1. Move from Beach to Jungle.
2. Collect the Rope.
3. Take the safe route to the Cave.
4. Search carefully and collect the Lantern.
5. Move to the Old Bridge.
6. Cross carefully.
7. Activate the Lighthouse beacon.

This route leaves the player with 1 energy point.

## Running the Tests

The project uses Python's built-in `unittest` framework.

Run all tests from the project root:

```bash
python3 -m unittest discover -s tests -v
```

Check Python syntax:

```bash
python3 -m py_compile main.py game.py tests/test_game.py tests/test_main.py
```

The tests cover game initialization, movement, item collection, inventory requirements, energy costs, invalid decisions, victory, defeat, and replay behaviour.

## Design and Architecture

The project separates terminal interaction from game rules:

- `main.py` manages what the player sees and how the player interacts with the game.
- `game.py` manages the underlying game state and rules.
- The test files verify the behaviour of the game and application.

This separation makes the game easier to maintain, test, and extend.

## Known Limitations

- The game is designed for one player at a time.
- Gameplay takes place entirely in the terminal.
- The island follows a fixed, forward-only route.
- Player progress is not saved between application runs.
- The game uses predefined locations, items, and decisions rather than randomly generated content.

## Future Improvements

Possible future extensions include:

- Save and resume functionality.
- Additional locations and puzzles.
- More branching decisions and endings.
- Random island events.
- Improved terminal presentation.

## Author

Developed as a Python programming and software engineering project.

GitHub repository: https://github.com/Aocheg/mystery-island-adventure

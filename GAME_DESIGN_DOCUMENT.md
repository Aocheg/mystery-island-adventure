
# MYSTERY ISLAND ADVENTURE
## Game Design Document

## 1. Game Overview

**Title:** Mystery Island Adventure

**Genre:** Text-based adventure / survival

**Platform:** Command-line terminal

**Programming Language:** Python

**Target Experience:** A simple interactive survival adventure in which players explore locations, collect items, make decisions, and manage limited resources to escape an island.

### Game Premise

A terrible storm destroys the player's ship, leaving the survivor stranded on a mysterious island.

The island contains several locations, obstacles, and useful objects. A lighthouse stands at the end of the island, but its beacon is inactive.

The player must collect the objects needed to overcome obstacles and restore the beacon so that a rescue boat can locate the island.

The player must manage limited energy throughout the journey. Poor decisions can cause the player to run out of energy before reaching safety.

## 2. Game Objective

The primary objective is to reach the Lighthouse and activate its beacon using the Lantern.

To achieve this, the player must:

1. Travel through the island's locations.
2. Collect the Rope in the Jungle.
3. Use the Rope to overcome the bridge obstacle.
4. Collect the Lantern in the Cave.
5. Use the Lantern to activate the Lighthouse beacon.
6. Preserve enough energy to complete the journey.

The player wins by activating the beacon with energy remaining.

The player loses when energy reaches zero.

## 3. Island Map and Progression

The game contains five locations connected in a fixed forward sequence.

```text
+---------+
|  Beach  |
+---------+
     |
     v
+---------+
| Jungle  |
+---------+
     |
     v
+---------+
|  Cave   |
+---------+
     |
     v
+------------+
| Old Bridge |
+------------+
     |
     v
+------------+
| Lighthouse |
+------------+
```

### Location descriptions

| Location | Description | Important requirement |
|---|---|---|
| Beach | A quiet beach where the player begins after the shipwreck | Starting point |
| Jungle | A dense jungle containing a useful rope | Collect Rope before leaving |
| Cave | A dark cave containing an old lantern | Find Lantern before leaving |
| Old Bridge | A dangerous wooden bridge across a deep valley | Rope is required |
| Lighthouse | An abandoned lighthouse with an inactive beacon | Lantern is required to activate beacon |

The player cannot skip locations or travel backwards.

## 4. Player State

Each new adventure creates a player state containing:

| Attribute | Initial value | Purpose |
|---|---|---|
| Name | Entered by player | Identifies the survivor |
| Location | Beach | Tracks current position |
| Energy | 5 | Tracks remaining survival energy |
| Inventory | Empty list | Stores collected objects |
| Game over | False | Tracks whether the adventure has ended |
| Won | False | Tracks whether the player escaped successfully |

A replay creates a new player state rather than reusing the previous adventure's state.

## 5. Inventory and Collectible Items

The game contains two essential collectible objects.

### Rope

- Location: Jungle.
- Collection cost: 0 energy.
- Purpose: Required to leave the Jungle and cross the Old Bridge.
- The Rope is not consumed when used.

### Lantern

- Location: Cave.
- Collection cost: Depends on the player's search decision.
- Purpose: Required to leave the Cave and activate the Lighthouse beacon.
- The Lantern is not consumed when used.

Each item can only be collected once.

The player cannot leave the Jungle without the Rope or leave the Cave without the Lantern.

## 6. Energy Management

The player begins with five energy points.

Energy represents the survivor's remaining strength and ability to continue exploring.

### Energy costs

| Action | Energy cost |
|---|---:|
| Beach to Jungle | 1 |
| Safe Jungle route | 1 |
| Dangerous Jungle shortcut | 2 |
| Careful Cave search | 0 additional |
| Rushed Cave search | 1 additional |
| Cave to Old Bridge | 1 |
| Careful bridge crossing | 1 |
| Rushed bridge crossing | 2 |
| Collect Rope | 0 |
| Check inventory | 0 |
| Check status | 0 |
| Invalid action | 0 |
| Activate beacon | 0 |

### Energy rules

1. Energy must never become negative.
2. An action cannot be completed if its energy cost exceeds the player's remaining energy.
3. A valid action that reduces energy to zero immediately ends the game in defeat.
4. The player cannot perform additional actions after game over.
5. The Lighthouse beacon can only be activated when the player has positive energy.
6. Victory requires at least one remaining energy point.

### Minimum-cost winning route

The minimum-cost winning route is:

| Stage | Energy before | Cost | Energy after |
|---|---:|---:|---:|
| Start at Beach | 5 | 0 | 5 |
| Move to Jungle | 5 | 1 | 4 |
| Collect Rope | 4 | 0 | 4 |
| Take safe route to Cave | 4 | 1 | 3 |
| Search carefully for Lantern | 3 | 0 | 3 |
| Move to Old Bridge | 3 | 1 | 2 |
| Cross carefully | 2 | 1 | 1 |
| Activate beacon | 1 | 0 | 1 |

This demonstrates that a successful adventure is possible with careful resource management.

## 7. Meaningful Player Decisions

The game contains three major decisions with different energy consequences.

### Decision 1: Jungle route

The player chooses between:

- Safe route: costs 1 energy.
- Dangerous shortcut: costs 2 energy.

Both routes lead to the Cave.

### Decision 2: Cave search

The player chooses between:

- Careful search: no additional energy cost.
- Rushed search: costs 1 additional energy.

Both approaches can find the Lantern.

### Decision 3: Old Bridge crossing

The player chooses between:

- Careful crossing: costs 1 energy.
- Rushed crossing: costs 2 energy.

Both approaches can cross the bridge if the player has the Rope.

These decisions allow different routes to have different survival consequences.

## 8. Game Menus and Player Actions

The player interacts with the game through numbered terminal menus.

### Standard location menu

1. Explore
2. Check surroundings
3. Collect item
4. Check inventory
5. Check status
6. Quit

### Lighthouse menu

1. Explore
2. Check surroundings
3. Collect item
4. Check inventory
5. Activate lighthouse beacon
6. Check status
7. Quit

### Action descriptions

**Explore:** Attempts to move the player to the next location. Special decisions are presented when required.

**Check surroundings:** Displays the current location description and relevant nearby objects.

**Collect item:** Attempts to collect the item available at the current location.

**Check inventory:** Displays the player's collected objects.

**Check status:** Displays the player's name, current location, energy, and inventory.

**Activate lighthouse beacon:** Checks the player's location, inventory, and energy before allowing victory.

**Quit:** Ends the current adventure.

## 9. Input Validation and Error Handling

The game should handle unexpected input without crashing.

Examples include:

- Invalid menu selections.
- Invalid route choices.
- Invalid search decisions.
- Invalid bridge-crossing decisions.
- Empty player names.
- Invalid replay responses.

Invalid actions must not deduct energy or change the player's location or inventory.

An empty player name defaults to "Survivor".

Replay responses accept `y`, `yes`, `n`, and `no`, without depending on letter case.

## 10. Game Outcomes

### Victory

The player wins when:

- The player is at the Lighthouse.
- The Lantern is in the inventory.
- The player has positive energy.
- The beacon is successfully activated.

The game displays a rescue message and congratulates the player.

### Defeat

The player loses when energy reaches zero.

The game displays a game-over message and explains that the survivor has run out of energy.

### Quit

The player can end the current adventure using the Quit menu option.

After the adventure ends, the application asks whether the player wants to replay.

## 11. Replay System

The replay system allows the player to begin another adventure after the current one ends.

When the player chooses to replay:

- The player is asked for a name again.
- The location returns to Beach.
- Energy resets to five.
- Inventory becomes empty.
- Game-over status resets to false.
- Victory status resets to false.

The previous adventure's state must not carry over.

## 12. Technical Architecture

The project separates game logic from terminal interaction.

### `main.py`

Responsible for:

- Displaying the introduction and instructions.
- Collecting the player's name.
- Displaying menus.
- Reading and processing player input.
- Displaying inventory and status.
- Managing the main gameplay loop.
- Handling victory, defeat, quit, and replay.

### `game.py`

Responsible for:

- Creating a new player state.
- Tracking player location and inventory.
- Managing energy.
- Validating movement.
- Validating item collection.
- Enforcing progression requirements.
- Checking Lighthouse activation requirements.
- Determining game outcomes.

### `tests/test_game.py`

Responsible for testing the underlying game rules and state transitions.

### `tests/test_main.py`

Responsible for testing application-level behaviour, including replay and invalid replay responses.

## 13. Testing Strategy

The project uses Python's built-in `unittest` framework.

Tests cover:

- Initial player state.
- Valid and invalid movement.
- Location progression.
- Item collection.
- Duplicate item prevention.
- Required inventory checks.
- Energy costs.
- Insufficient energy.
- Zero-energy defeat.
- Victory conditions.
- Replay behaviour.
- Invalid replay responses.

Run the complete test suite using:

```bash
python3 -m unittest discover -s tests -v
```

## 14. Constraints and Future Development

### Current constraints

- Terminal-only interface.
- One player per adventure.
- Fixed location sequence.
- No persistent save system.
- Predefined events and collectible objects.

### Possible future improvements

- More locations and branching paths.
- Additional items and puzzles.
- Save and resume functionality.
- Randomized events.
- More possible endings.
- Improved terminal interface.

## 15. Definition of Done

The project is considered complete when:

1. The game starts using `python3 main.py`.
2. The player can enter a name and see instructions.
3. All five locations are accessible in the correct sequence.
4. The Rope and Lantern can be collected.
5. Inventory requirements are enforced.
6. Energy costs and consequences work correctly.
7. Invalid input does not crash the game.
8. Both victory and defeat are possible.
9. The player can quit and replay.
10. A replay creates a fresh player state.
11. Automated tests pass.
12. The README explains setup, gameplay, and testing.

---

**Project:** Mystery Island Adventure

**Implementation language:** Python

**Interface:** Command-line terminal

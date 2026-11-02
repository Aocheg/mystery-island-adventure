
# ==========================================
# MYSTERY ISLAND ADVENTURE
# Core Game Logic
# ==========================================

# SECTION 1: Island locations

LOCATION_ROUTE = {
    "Beach": "Jungle",
    "Jungle": "Cave",
    "Cave": "Old Bridge",
    "Old Bridge": "Lighthouse"
}

LOCATION_DESCRIPTIONS = {
    "Beach": (
        "You are standing on a quiet beach. "
        "The sound of waves fills the air."
    ),
    "Jungle": (
        "You have entered a dense jungle. "
        "Tall trees surround you, and strange sounds "
        "come from the bushes."
    ),
    "Cave": (
        "You have discovered a dark cave. "
        "The entrance is narrow, and you can barely "
        "see what lies inside."
    ),
    "Old Bridge": (
        "You have reached an old wooden bridge. "
        "It stretches across a deep, dangerous valley."
    ),
    "Lighthouse": (
        "You have arrived at the abandoned lighthouse. "
        "Its beacon is dark. You must restore it to "
        "signal the rescue boat."
    )
}

# SECTION 2: Items and their locations

LOCATION_ITEMS = {
    "Jungle": "Rope",
    "Cave": "Lantern"
}

# SECTION 3: Initialize a new game

def new_game(player_name):
    """Create and return a new game state."""
    return {
        "name": player_name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }


# SECTION 4: Energy management

def spend_energy(player, cost):
    """Deduct energy and handle insufficient or exhausted energy."""

    if cost < 0:
        return False, "Energy cost cannot be negative."

    if player["game_over"]:
        return False, "The game has already ended."

    if cost > player["energy"]:
        return False, (
            f"Not enough energy. You need {cost}, "
            f"but you only have {player['energy']}."
        )

    player["energy"] -= cost

    if player["energy"] == 0:
        player["game_over"] = True
        player["won"] = False

        return True, (
            "You have exhausted all your energy. "
            "You collapse from exhaustion.\n"
            "GAME OVER!"
        )

    return True, f"You spent {cost} energy."


# SECTION 5: Inventory and puzzle checks

def can_cross_bridge(player):
    """Check whether the player has the rope."""
    return "Rope" in player["inventory"]


def can_light_lighthouse(player):
    """Check whether the player has the lantern."""
    return "Lantern" in player["inventory"]


# SECTION 6: Collect items

def collect_item(player, approach="careful"):
    """Collect an available item at the current location."""

    if player["game_over"]:
        return False, "The game has already ended."

    location = player["location"]
    item = LOCATION_ITEMS.get(location)

    if item is None:
        return False, "There are no useful items to collect here."

    if item in player["inventory"]:
        return False, f"You have already collected the {item}."

    # Searching for the lantern has two possible approaches.
    if location == "Cave":
        if approach == "careful":
            cost = 0
        elif approach == "rushed":
            cost = 1
        else:
            return False, "Choose either a careful or rushed search."

        energy_success, energy_message = spend_energy(player, cost)

        if not energy_success:
            return False, energy_message

        player["inventory"].append(item)

        if player["game_over"]:
            return True, (
                "You found the lantern, but the rushed search "
                "used your last energy.\n"
                "GAME OVER!"
            )

        if approach == "careful":
            return True, (
                "You carefully search the cave and find the Lantern!"
            )

        return True, (
            "You rush through the cave and find the Lantern!\n"
            f"{energy_message} Energy remaining: {player['energy']}."
        )

    # Collecting the rope has no energy cost.
    player["inventory"].append(item)

    return True, f"You collected the {item}!"


# SECTION 7: Handle player movement

def move_player(player, destination, choice="safe"):
    """Validate movement, apply energy costs and update location."""

    if player["game_over"]:
        return False, "The game has already ended."

    current_location = player["location"]
    next_location = LOCATION_ROUTE.get(current_location)

    if next_location is None:
        return False, "There are no further locations to explore."

    if destination != next_location:
        return False, "You cannot travel in that direction."

    # Check the Jungle rope requirement.
    if current_location == "Jungle" and not can_cross_bridge(player):
        return False, "You need to collect the rope before leaving the Jungle."

    # Check the Cave lantern requirement.
    if current_location == "Cave" and not can_light_lighthouse(player):
        return False, "You need to find the lantern before leaving the Cave."

    # Check the Old Bridge rope requirement.
    if current_location == "Old Bridge" and not can_cross_bridge(player):
        return False, "You need the rope to cross the Old Bridge."

    # Determine the energy cost of the movement.
    if current_location == "Beach":
        cost = 1

    elif current_location == "Jungle":
        if choice == "safe":
            cost = 1
        elif choice == "dangerous":
            cost = 2
        else:
            return False, "Choose either the safe route or dangerous shortcut."

    elif current_location == "Cave":
        cost = 1

    elif current_location == "Old Bridge":
        if choice == "careful":
            cost = 1
        elif choice == "rushed":
            cost = 2
        else:
            return False, "Choose either a careful or rushed crossing."

    else:
        return False, "Movement is not available here."

    energy_success, energy_message = spend_energy(player, cost)

    if not energy_success:
        return False, energy_message

    # Complete movement after successful energy deduction.
    player["location"] = destination

    if player["game_over"]:
        return True, (
            f"You reached {destination}, but the journey "
            "used your last energy.\nGAME OVER!"
        )

    return True, (
        f"You have arrived at {destination}.\n"
        f"{energy_message} Energy remaining: {player['energy']}."
    )


# SECTION 8: Activate the lighthouse

def activate_beacon(player):
    """Activate the lighthouse if the player has the lantern."""

    if player["game_over"]:
        return False, "The game has already ended."

    if player["location"] != "Lighthouse":
        return False, "You must reach the Lighthouse first."

    if not can_light_lighthouse(player):
        return False, "You need the lantern to restore the lighthouse beacon."

    if player["energy"] <= 0:
        return False, "You need energy remaining to complete your escape."

    player["won"] = True
    player["game_over"] = True

    return True, (
        "You use the lantern to restore the lighthouse beacon!\n"
        "A rescue boat spots your signal and heads towards the island.\n"
        "CONGRATULATIONS! YOU HAVE ESCAPED MYSTERY ISLAND!"
    )

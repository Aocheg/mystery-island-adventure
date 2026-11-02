
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

# SECTION 4: Collect items

def collect_item(player):
    """Collect an available item at the current location."""
    location = player["location"]
    item = LOCATION_ITEMS.get(location)

    if item is None:
        return False, "There are no useful items to collect here."

    if item in player["inventory"]:
        return False, f"You have already collected the {item}."

    player["inventory"].append(item)

    return True, f"You collected the {item}!"

# SECTION 5: Inventory and puzzle checks

def can_cross_bridge(player):
    """Check whether the player has the rope."""
    return "Rope" in player["inventory"]


def can_light_lighthouse(player):
    """Check whether the player has the lantern."""
    return "Lantern" in player["inventory"]


# SECTION 6: Handle player movement

def move_player(player, destination):
    """Validate and execute movement to the next location."""
    current_location = player["location"]
    next_location = LOCATION_ROUTE.get(current_location)

    if next_location is None:
        return False, "There are no further locations to explore."

    if destination != next_location:
        return False, "You cannot travel in that direction."

    # The rope is required to leave the Jungle.
    if current_location == "Jungle" and not can_cross_bridge(player):
        return False, "You need to collect the rope before leaving the Jungle."

    # The lantern is required to leave the Cave.
    if current_location == "Cave" and not can_light_lighthouse(player):
        return False, "You need to find the lantern before leaving the Cave."

    # The rope is also required to cross the Old Bridge.
    if current_location == "Old Bridge" and not can_cross_bridge(player):
        return False, "You need the rope to cross the Old Bridge."

    player["location"] = destination

    return True, f"You have arrived at {destination}."


# SECTION 7: Activate the lighthouse

def activate_beacon(player):
    """Activate the lighthouse if the player has the lantern."""
    if player["location"] != "Lighthouse":
        return False, "You must reach the Lighthouse first."

    if not can_light_lighthouse(player):
        return False, "You need the lantern to restore the lighthouse beacon."

    player["won"] = True
    player["game_over"] = True

    return True, (
        "You use the lantern to restore the lighthouse beacon!\n"
        "A rescue boat spots your signal and heads towards the island.\n"
        "CONGRATULATIONS! YOU HAVE ESCAPED MYSTERY ISLAND!"
    )

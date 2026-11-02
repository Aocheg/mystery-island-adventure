
# ==========================================
# MYSTERY ISLAND ADVENTURE
# Main Application
# ==========================================

from game import (
    new_game,
    move_player,
    collect_item,
    activate_beacon,
    LOCATION_ROUTE,
    LOCATION_DESCRIPTIONS
)


# SECTION 1: Display the introduction

def show_intro():
    """Display the game title and introduction."""
    print("=" * 40)
    print("          MYSTERY ISLAND")
    print("=" * 40)
    print("\nA terrible storm has destroyed your ship.")
    print("You wake up stranded on a mysterious island.")
    print("Your journey to survival begins here.")


# SECTION 2: Start a new game

def start_game():
    """Initialize the player and start the game."""
    show_intro()

    player_name = input("\nWhat is your name, survivor? ").strip()

    if not player_name:
        player_name = "Survivor"

    player = new_game(player_name)

    print(f"\nWelcome, {player_name}.")
    print("Your survival journey starts now!")

    print(f"\nStarting Location: {player['location'].upper()}")
    print(LOCATION_DESCRIPTIONS[player["location"]])

    return player


# SECTION 3: Display the menu

def show_menu(player):
    """Display available actions at the current location."""
    location = player["location"]

    print(f"\n========== {location.upper()} MENU ==========")
    print("1. Explore")
    print("2. Check surroundings")
    print("3. Collect item")
    print("4. Check inventory")

    if location == "Lighthouse":
        print("5. Activate lighthouse beacon")
        print("6. Quit")
    else:
        print("5. Quit")


# SECTION 4: Display inventory

def display_inventory(player):
    """Display all collected items."""
    inventory = player["inventory"]

    print("\n========== INVENTORY ==========")

    if not inventory:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item}")


# SECTION 5: Handle player actions

def handle_choice(player, choice):
    """Process the player's selected menu option."""

    if choice == "1":
        current_location = player["location"]
        destination = LOCATION_ROUTE.get(current_location)

        if destination is None:
            print("\nThere are no further locations to explore.")
            return

        success, message = move_player(player, destination)

        print(f"\n{message}")

        if success:
            print(LOCATION_DESCRIPTIONS[player["location"]])

    elif choice == "2":
        location = player["location"]

        print("\nYou examine your surroundings.")
        print(LOCATION_DESCRIPTIONS[location])

        if location == "Jungle" and "Rope" not in player["inventory"]:
            print("You notice a strong rope lying near a tree.")

        elif location == "Cave" and "Lantern" not in player["inventory"]:
            print("You notice an old lantern inside the cave.")

    elif choice == "3":
        success, message = collect_item(player)
        print(f"\n{message}")

    elif choice == "4":
        display_inventory(player)

    elif choice == "5" and player["location"] == "Lighthouse":
        success, message = activate_beacon(player)
        print(f"\n{message}")

    elif choice == "5":
        print(f"\nGoodbye, {player['name']}.")
        print("Your adventure ends here.")
        player["game_over"] = True

    elif choice == "6" and player["location"] == "Lighthouse":
        print(f"\nGoodbye, {player['name']}.")
        print("Your adventure ends here.")
        player["game_over"] = True

    else:
        print("\nInvalid choice. Please select an available menu option.")


# SECTION 6: Main game loop

def main():
    """Run the main game application."""
    player = start_game()

    while not player["game_over"]:
        show_menu(player)

        choice = input("\nWhat would you like to do? ").strip()

        handle_choice(player, choice)

    if player["won"]:
        print("\nThank you for completing Mystery Island!")
    else:
        print("\nThank you for playing Mystery Island!")


# SECTION 7: Application entry point

if __name__ == "__main__":
    main()

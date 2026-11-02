
# MYSTERY ISLAND
# A text-based adventure game

print("=" * 40)
print("          MYSTERY ISLAND")
print("=" * 40)

print("\nA terrible storm has destroyed your ship.")
print("You wake up stranded on a mysterious island.")
print("Your journey to survival begins here.")

print("\nStarting Location: BEACH")
print("You are standing on a quiet beach.")
print("The sound of waves fills the air.")


player_name = input("\nWhat is your name, survivor? ")

print(f"\nWelcome, {player_name}.")
print("Your survival journey starts now!")


while True:
    print("\n========== BEACH MENU ==========")
    print("1. Explore")
    print("2. Check surroundings")
    print("3. Quit")

    choice = input("\nWhat would you like to do? ")

    if choice == "1":
        print("\nYou look around the beach.")
        print("Exploration will be available in the next stage.")

    elif choice == "2":
        print("\nYou examine your surroundings.")
        print("You see the ocean, some rocks, and an abandoned ship.")

    elif choice == "3":
        print(f"\nGoodbye, {player_name}. Your adventure ends here.")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")

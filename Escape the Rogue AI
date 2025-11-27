# Escape the Rogue AI - Numbered Menu Version

# ---------- GAME DATA ----------

rooms = {
    "Dorm Room": {
        "East": "Hallway",
        "South": "Security Office",
        "item": None
    },
    "Hallway": {
        "West": "Dorm Room",
        "East": "Computer Lab",
        "item": "Keycard"
    },
    "Computer Lab": {
        "West": "Hallway",
        "East": "Rooftop Antenna",
        "South": "Network Closet",
        "item": "Laptop"
    },
    "Rooftop Antenna": {
        "West": "Computer Lab",
        "item": "Signal Booster"
    },
    "Security Office": {
        "North": "Dorm Room",
        "East": "Server Room",
        "item": "Access Codes"
    },
    "Server Room": {
        "West": "Security Office",
        "East": "Network Closet",
        "item": "Debugging Toolkit"
    },
    "Network Closet": {
        "West": "Server Room",
        "North": "Computer Lab",
        "East": "Mainframe Core",
        "item": "Ethernet Cable"
    },
    "Mainframe Core": {
        "West": "Network Closet",
        "item": None  # Villain room, no item
    }
}

VILLAIN_ROOM = "Mainframe Core"
TOTAL_ITEMS_NEEDED = 6


# ---------- HELPER FUNCTIONS ----------

def show_intro():
    print("Escape the Rogue AI")
    print("Collect 6 items to win the game, then enter the Mainframe Core.")
    print("If you enter the Mainframe Core without all 6 items, the Rogue AI defeats you.")
    print("-" * 40)


def show_status(current_room, inventory):
    """Display the player's current status."""
    print("\n---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    room_item = rooms[current_room].get("item")
    if room_item is not None and room_item not in inventory:
        print(f"You see a {room_item}")


def show_options(current_room, inventory):
    """
    Build and display a numbered list of options.
    Returns a list of (description, action_type, action_value).
    action_type is 'move', 'get', or 'exit'.
    """
    room_data = rooms[current_room]
    room_item = room_data.get("item")

    print("\nChoose an option:")
    options = []  # list of (description, action_type, action_value)

    # Movement options in NSEW order
    for direction in ["North", "South", "East", "West"]:
        if direction in room_data:
            next_room = room_data[direction]
            desc = f"Go {direction} → {next_room}"
            options.append((desc, "move", direction))

    # Item option
    if room_item is not None and room_item not in inventory:
        desc = f"Pick up {room_item}"
        options.append((desc, "get", room_item))

    # Exit game option
    options.append(("Exit Game", "exit", None))

    # Display with numbers
    for i, (desc, _, _) in enumerate(options, start=1):
        print(f"{i}. {desc}")

    return options


def move_player(current_room, direction):
    """
    Try to move the player in the given direction.
    Returns (new_current_room, message).
    """
    room_data = rooms[current_room]
    if direction in room_data:
        new_room = room_data[direction]
        return new_room, f"You move to the {new_room}."
    else:
        return current_room, "You can't go that way!"


def get_item(current_room, inventory, room_item):
    """
    Handle getting an item from the current room.
    room_item is already the correct item for this room.
    Returns a message string.
    """
    # If the item is somehow None (shouldn't be if we called this correctly)
    if room_item is None:
        return "There is no item to get in this room."

    if room_item in inventory:
        return f"You already picked up the {room_item}."

    inventory.append(room_item)

    if len(inventory) == TOTAL_ITEMS_NEEDED:
        return (f"{room_item} retrieved! You now have all 6 items. "
                "Go to the Mainframe Core to defeat the Rogue AI.")
    else:
        return f"{room_item} retrieved!"


# ---------- MAIN GAME LOOP ----------

def main():
    current_room = "Dorm Room"
    inventory = []
    game_active = True

    show_intro()

    while game_active:
        show_status(current_room, inventory)

        # Show numbered options
        options = show_options(current_room, inventory)

        choice = input("\nEnter your choice number: ").strip()

        # Validate numeric choice
        if not choice.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        choice_num = int(choice)

        if choice_num < 1 or choice_num > len(options):
            print("Invalid choice! Please pick a valid option number.")
            continue

        # Unpack the chosen option
        desc, action_type, action_value = options[choice_num - 1]

        if action_type == "move":
            # action_value is a direction like "East"
            current_room, msg = move_player(current_room, action_value)
            print(msg)

            # Check villain encounter
            if current_room == VILLAIN_ROOM:
                if len(inventory) == TOTAL_ITEMS_NEEDED:
                    print("You confront the Rogue AI with all your tools!")
                    print("You upload the patch and shut down the AI. YOU WIN!")
                else:
                    print("The Rogue AI overwhelms you...")
                    print("NOM NOM...GAME OVER!")
                game_active = False

        elif action_type == "get":
            # action_value is the correct item name for this room
            room_item = action_value
            msg = get_item(current_room, inventory, room_item)
            print(msg)

        elif action_type == "exit":
            print("Thanks for playing! Goodbye.")
            game_active = False

    print("\nGame ended.")


if __name__ == "__main__":
    main()

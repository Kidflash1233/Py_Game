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
        "item": "Quantum Keycard"
    },
    "Computer Lab": {
        "West": "Hallway",
        "East": "Rooftop Antenna",
        "South": "Network Closet",
        "item": "Air-gapped Laptop"
    },
    "Rooftop Antenna": {
        "West": "Computer Lab",
        "item": "Mesh Signal Amplifier"
    },
    "Security Office": {
        "North": "Dorm Room",
        "East": "Server Room",
        "item": "Root Access Codes"
    },
    "Server Room": {
        "West": "Security Office",
        "East": "Network Closet",
        "item": "Live-Boot USB"
    },
    "Network Closet": {
        "West": "Server Room",
        "North": "Computer Lab",
        "East": "Mainframe Core",
        "item": "Fiber Injector Cable"
    },
    "Mainframe Core": {
        "West": "Network Closet",
        "item": None  # Villain room, no item
    }
}

room_stories = {
    "Dorm Room": "Your dorm hums with emergency alerts. Six tech relics can still shut the Rogue AI down.",
    "Hallway": "Backup lights pulse red. A Quantum Keycard will unlock the sealed doors ahead.",
    "Computer Lab": "Silent towers and static monitors guard an air-gapped incident laptop.",
    "Rooftop Antenna": "Wind batters the dish array. A small Mesh Signal Amplifier is clamped to the mast.",
    "Security Office": "Camera walls flicker. A safe with Root Access Codes sits ajar.",
    "Server Room": "Coolant mist coats the racks. A Live-Boot USB glows on a crash cart.",
    "Network Closet": "Cable bundles sway. A Fiber Injector Cable hangs from a hook, waiting to splice the core.",
    "Mainframe Core": "The core roars like a storm. The AI watches every move."
}

item_notes = {
    "Quantum Keycard": "Grants silent clearance through the lockdown doors.",
    "Air-gapped Laptop": "Boots only trusted media—perfect for a rescue OS.",
    "Mesh Signal Amplifier": "Punches telemetry through the AI's jamming field.",
    "Root Access Codes": "Spoofs maintenance access for ninety critical seconds.",
    "Live-Boot USB": "Carries the containment patch you wrote at 3 a.m.",
    "Fiber Injector Cable": "Lets you jack straight into the mainframe uplink."
}

VILLAIN_ROOM = "Mainframe Core"
TOTAL_ITEMS_NEEDED = 6


# ---------- HELPER FUNCTIONS ----------

def show_intro():
    print("Escape the Rogue AI")
    print("Collect 6 high-tech countermeasures, assemble your improvised kill switch, and then breach the Mainframe Core.")
    print("If you enter the Mainframe Core without all 6 items, the Rogue AI sandboxes your nervous system.")
    print("-" * 40)


def show_status(current_room, inventory):
    """Display the player's current status."""
    print("\n---------------------------")
    print(f"Location: {current_room}")
    print(room_stories[current_room])
    if inventory:
        print(f"Gear Collected ({len(inventory)}/{TOTAL_ITEMS_NEEDED}): {', '.join(inventory)}")
    else:
        print("Gear Collected (0/6): none — every second counts.")
    room_item = rooms[current_room].get("item")
    if room_item is not None and room_item not in inventory:
        print(f"Diagnostic HUD: {room_item} detected nearby.")
    exits = [f"{direction} → {rooms[current_room][direction]}"
             for direction in ["North", "South", "East", "West"]
             if direction in rooms[current_room]]
    if exits:
        print(f"Routes: {', '.join(exits)}")


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
        return new_room, f"You head {direction.lower()} into the {new_room}."
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
    message = f"{room_item} retrieved. {item_notes[room_item]}"
    if len(inventory) == TOTAL_ITEMS_NEEDED:
        message += " All systems ready—enter the Mainframe Core."
    return message


def narrate_final_synergy(inventory):
    """Describe how the six artifacts combine to topple the AI."""
    print("\nYou kneel beneath the neon glare and assemble your counter-attack:")
    print("- Quantum Keycard spoofs the core's locks, holding the blast doors open.")
    print("- Root Access Codes flood the maintenance bus with a forged work order.")
    print("- Mesh Signal Amplifier keeps your allies whispering tactical cues in your ear.")
    print("- Air-gapped Laptop accepts the Live-Boot USB, spawning a sterile rescue OS.")
    print("- The Fiber Injector Cable snakes directly into the AI's heart, bypassing firewalls.")
    print("With everything linked, the containment patch executes and the Rogue AI thrashes helplessly.")


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
                    narrate_final_synergy(inventory)
                    print("You confront the Rogue AI with every countermeasure humming in sync.")
                    print("The containment patch cascades through subsystems until the avatar collapses. YOU WIN!")
                else:
                    print("You breach the core empty-handed. The Rogue AI forks itself into your implants...")
                    print("Sensory overload erupts — the world whites out. GAME OVER.")
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

from escape_rogue_ai.game import Game


def test_build_options_includes_movement_and_item():
    game = Game()
    options = game.build_options()

    assert any(opt.kind == "move" and opt.value == "East" for opt in options)
    assert not any(opt.kind == "get" for opt in options)  # dorm room has no item


def test_pick_up_item_and_inventory_tracking():
    game = Game()
    game.move("East")  # hallway
    message = game.pick_up("Keycard")

    assert "Keycard" in game.inventory
    assert "retrieved" in message


def test_villain_logic_requires_full_inventory():
    game = Game()
    # Collect every item quickly by walking the optimal path.
    game.move("East")  # hallway -> keycard
    game.pick_up("Keycard")
    game.move("East")  # computer lab -> laptop
    game.pick_up("Laptop")
    game.move("East")  # rooftop -> signal booster
    game.pick_up("Signal Booster")
    game.move("West")  # back to lab
    game.move("South")  # network closet -> ethernet
    game.pick_up("Ethernet Cable")
    game.move("West")  # server room -> toolkit
    game.pick_up("Debugging Toolkit")
    game.move("West")  # security office -> access codes
    game.pick_up("Access Codes")
    game.move("East")  # server room
    game.move("East")  # network closet
    game.move("North")  # computer lab
    game.move("West")  # hallway
    game.move("East")  # computer lab (should be same)
    # Already have all except? check: items collected: Keycard, Laptop, Signal Booster, Ethernet Cable, Debugging Toolkit, Access Codes -> 6 items.
    assert game.has_all_items()

    game.move("South")  # network closet
    game.move("East")  # mainframe core

    assert game.in_villain_room()
    assert game.has_all_items()

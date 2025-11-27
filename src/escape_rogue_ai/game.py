"""Core game logic for Escape the Rogue AI."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable, Literal, Sequence

from .data import ROOMS, START_ROOM, TOTAL_ITEMS_NEEDED, VILLAIN_ROOM, Room

Direction = Literal["North", "South", "East", "West"]
OptionType = Literal["move", "get", "exit"]


@dataclass(frozen=True)
class Option:
    """Represents an action the player can choose."""

    description: str
    kind: OptionType
    value: str | None = None


@dataclass
class Game:
    """Mutable game state with helper methods for the CLI layer."""

    current_room: str = START_ROOM
    inventory: list[str] = field(default_factory=list)

    def room(self) -> Room:
        return ROOMS[self.current_room]

    def build_options(self) -> list[Option]:
        """Return the available options in NSEW/get order."""
        ordered_directions: Sequence[Direction] = ("North", "South", "East", "West")
        options: list[Option] = []

        for direction in ordered_directions:
            destination = self.room().connections.get(direction)
            if destination:
                desc = f"Go {direction} → {destination}"
                options.append(Option(desc, "move", direction))

        item = self.room().item
        if item and item not in self.inventory:
            options.append(Option(f"Pick up {item}", "get", item))

        options.append(Option("Exit Game", "exit"))
        return options

    def status_lines(self) -> list[str]:
        """Return the textual representation of the current status."""
        lines = [
            "---------------------------",
            f"You are in the {self.current_room}",
            f"Inventory: {self.inventory}",
        ]

        item = self.room().item
        if item and item not in self.inventory:
            lines.append(f"You see a {item}")

        return lines

    def move(self, direction: Direction) -> str:
        """Move the player to a connected room."""
        destination = self.room().connections.get(direction)
        if not destination:
            raise ValueError(f"Cannot go {direction} from {self.current_room}.")

        self.current_room = destination
        return f"You move to the {destination}."

    def pick_up(self, item: str) -> str:
        """Collect an item from the current room."""
        room_item = self.room().item
        if not room_item or room_item != item:
            raise ValueError("There is no item to collect here.")
        if item in self.inventory:
            return f"You already picked up the {item}."

        self.inventory.append(item)
        if len(self.inventory) == TOTAL_ITEMS_NEEDED:
            return (
                f"{item} retrieved! You now have all {TOTAL_ITEMS_NEEDED} items. "
                "Head to the Mainframe Core to defeat the Rogue AI."
            )
        return f"{item} retrieved!"

    def in_villain_room(self) -> bool:
        return self.current_room == VILLAIN_ROOM

    def has_all_items(self) -> bool:
        return len(self.inventory) == TOTAL_ITEMS_NEEDED


def _print_intro() -> None:
    print("Escape the Rogue AI")
    print("Collect six items and then make your way to the Mainframe Core.")
    print("Entering the Mainframe Core early lets the rogue AI win.")
    print("-" * 40)


def _prompt_choice(input_func: Callable[[str], str], count: int) -> int:
    raw = input_func("\nEnter your choice number: ").strip()
    if not raw.isdigit():
        raise ValueError("Please enter a valid number.")

    choice = int(raw)
    if choice < 1 or choice > count:
        raise ValueError("Choice out of range.")
    return choice


def play(input_func: Callable[[str], str] = input) -> None:
    """Interactive CLI loop for the game."""
    game = Game()
    _print_intro()

    while True:
        for line in game.status_lines():
            print(line)

        options = game.build_options()
        print("\nChoose an option:")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option.description}")

        try:
            selected = _prompt_choice(input_func, len(options))
        except ValueError as exc:
            print(f"Invalid input! {exc}")
            continue

        option = options[selected - 1]
        if option.kind == "move":
            try:
                print(game.move(option.value))  # type: ignore[arg-type]
            except ValueError as exc:
                print(exc)
                continue

            if game.in_villain_room():
                if game.has_all_items():
                    print("You confront the Rogue AI with every tool!")
                    print("You upload the patch and shut down the AI. YOU WIN!")
                else:
                    print("The Rogue AI overwhelms you. NOM NOM...GAME OVER!")
                break

        elif option.kind == "get":
            try:
                print(game.pick_up(option.value or ""))
            except ValueError as exc:
                print(exc)

        elif option.kind == "exit":
            print("Thanks for playing! Goodbye.")
            break

    print("\nGame ended.")

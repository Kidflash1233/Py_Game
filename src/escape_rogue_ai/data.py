"""Static data that defines the Escape the Rogue AI map."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Room:
    """Represents a single location in the facility."""

    name: str
    connections: Mapping[str, str]
    item: str | None = None


ROOMS: dict[str, Room] = {
    "Dorm Room": Room(
        name="Dorm Room",
        connections={"East": "Hallway", "South": "Security Office"},
    ),
    "Hallway": Room(
        name="Hallway",
        connections={"West": "Dorm Room", "East": "Computer Lab"},
        item="Keycard",
    ),
    "Computer Lab": Room(
        name="Computer Lab",
        connections={
            "West": "Hallway",
            "East": "Rooftop Antenna",
            "South": "Network Closet",
        },
        item="Laptop",
    ),
    "Rooftop Antenna": Room(
        name="Rooftop Antenna",
        connections={"West": "Computer Lab"},
        item="Signal Booster",
    ),
    "Security Office": Room(
        name="Security Office",
        connections={"North": "Dorm Room", "East": "Server Room"},
        item="Access Codes",
    ),
    "Server Room": Room(
        name="Server Room",
        connections={"West": "Security Office", "East": "Network Closet"},
        item="Debugging Toolkit",
    ),
    "Network Closet": Room(
        name="Network Closet",
        connections={
            "West": "Server Room",
            "North": "Computer Lab",
            "East": "Mainframe Core",
        },
        item="Ethernet Cable",
    ),
    "Mainframe Core": Room(
        name="Mainframe Core",
        connections={"West": "Network Closet"},
    ),
}


START_ROOM = "Dorm Room"
VILLAIN_ROOM = "Mainframe Core"
TOTAL_ITEMS_NEEDED = 6

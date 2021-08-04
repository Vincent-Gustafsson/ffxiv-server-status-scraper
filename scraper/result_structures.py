from dataclasses import dataclass
from typing import Literal

WorldStatusString = Literal["online", "partial_maintenance", "maintenance"]
WorldCategory = Literal["standard", "preferred"]

@dataclass
class WorldInformation:
    name: str
    status: WorldStatusString
    category: WorldCategory
    can_create_character: bool

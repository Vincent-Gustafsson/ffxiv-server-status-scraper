from enum import IntEnum
from typing import Literal

from bs4.element import PageElement


WorldStatusString = Literal["online", "partial_maintenance", "maintenance"]

class WorldStatus(IntEnum):
    ONLINE = 1
    PARTIAL_MAINTENANCE = 2
    MAINTENANCE = 3


def get_world_status(world_item: PageElement) -> WorldStatusString:
    WORLD_STATUS_CLASS = "world-list__status_icon"
    status_icon_el = world_item.find(class_=WORLD_STATUS_CLASS).find("i")
    
    # The icon class name ends with a number.
    # example:
    #   "world-ic__1"
    #
    # 1 - Online
    # 2 - Partial Maintenance
    # 3 - Maintenance
    # 
    # This snippet extracts that number.
    world_status = int(status_icon_el["class"][0][-1])
    
    """TODO Python 3.10 pattern matching
    match server_status:
        case WorldStatus.ONLINE:
            return "online"
        
        case WorldStatus.PARTIAL_MAINTENANCE:
            return "partial_maintenance"
        
        case WorldStatus.MAINTENANCE:
            return "maintenance"
    """

    if world_status == WorldStatus.ONLINE:
        return "online"

    elif world_status == WorldStatus.PARTIAL_MAINTENANCE:
        return "partial_maintenance"

    elif world_status == WorldStatus.MAINTENANCE:
        return "maintenance"
    
    else:
        raise Exception("Fucky server status")


def get_world_can_create_character(world_item: PageElement) -> bool:
    WORLD_CREATE_CHARACTER_CLASS = "world-list__create_character"

    create_character_icon_el = world_item.find(class_=WORLD_CREATE_CHARACTER_CLASS).find("i")
    class_name = create_character_icon_el["class"][0]
    


    # Btw, would this even work?
    # Is this *how* it works?
    """TODO Python 3.10 pattern matching
    match ["available" in class_name, "unavailable" in class_name]:
        case True, False:
            return True
        case False, True:
            return False
        case _:
            raise Exception("Fucky create_character status")
    """
        


    if "unavailable" in class_name:
        return False

    elif "available" in class_name:
        return True
    
    else:
        # Not sure if I need this edge-case.
        # If not, I could just do:
        #   return "available" in create_character_class_name
        raise Exception("Fucky create_character status")

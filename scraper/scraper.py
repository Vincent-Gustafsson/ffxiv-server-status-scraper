from typing import Dict
from requests import Response
from bs4 import BeautifulSoup, SoupStrainer
from bs4.element import PageElement

from .result_structures import WorldInformation
from .helpers import get_world_can_create_character, get_world_status


# Sus typing, omitting return type.
def extract_region_tables(soup: BeautifulSoup):
    REGION_NAMES = ["jp", "na", "eu"]
    region_tables = soup.find_all(class_="world-dcgroup")

    return zip(REGION_NAMES, region_tables)


def extract_world_information(world_item: PageElement) -> WorldInformation:
    WORLD_NAME_CLASS = "world-list__world_name"
    WORLD_CATEGORY_CLASS = "world-list__world_category"

    # Get the name text and strip the \n from it.
    world_name = world_item.find(class_=WORLD_NAME_CLASS).text.strip()
    
    world_status = get_world_status(world_item)
    
    # Get the name text and strip the \n from it, and then make it lowercase.
    world_category = world_item.find(class_=WORLD_CATEGORY_CLASS).text.strip().lower()

    world_can_create_character = get_world_can_create_character(world_item)

    return WorldInformation(
        world_name,
        world_status,
        world_category,
        world_can_create_character
    )


def extract_data(regions: zip):
    result_data: Dict[str, Dict] = {
        "jp": {},
        "na": {},
        "eu": {}
    }

    for region, table in regions:
        # Find all datacenter lists with the corresponding worlds
        data_center_lists = table.find_all("li", class_="world-dcgroup__item")

        for data_center in data_center_lists:
            data_center_name = data_center.h2.text.lower()

            # Initialize a key-value pair where the key is the datacenter name,
            # and the value will be a list with all the worlds of that datacenter.
            result_data[region][data_center_name] = {}

            world_items = data_center.ul.find_all("li")

            for world in world_items:
                world_info: WorldInformation = extract_world_information(world)
                
                result_data[region][data_center_name][world_info.name] = {
                    "status": world_info.status,
                    "category": world_info.category,
                    "can_create_character": world_info.can_create_character
                }
    
    return result_data



def scrape(page: Response) -> Dict[str, Dict]:
    strainer = SoupStrainer(class_="world-dcgroup")
    soup = BeautifulSoup(page.content, "html.parser", parse_only=strainer)

    regions = extract_region_tables(soup)
    result = extract_data(regions)
    
    return result

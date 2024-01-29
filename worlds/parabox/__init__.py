import logging

from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from worlds.parabox.ap_opt_gen import ParaboxOptions
from worlds.parabox.ap_item_gen import item_name_to_id
from worlds.parabox.ap_preset_gen import options_presets

# from worlds.parabox.external.groups import item_name_groups

PARABOX_GAME = "Patrick's Parabox"
PARABOX_LOGGER = logging.getLogger(PARABOX_GAME)


class ParaboxWebWorld(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Patrick's Parabox Randomizer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Wiggel"]
    )]
    options_presets = options_presets


class ParaboxWorld(World):
    """
    Patrick's Parabox is a puzzle game
    that explores a unique recursive system
    of boxes within boxes within boxes within boxes.
    """
    game = PARABOX_GAME
    options_dataclass = ParaboxOptions
    options: ParaboxOptions
    web = ParaboxWebWorld()
    topology_present = False

    item_name_to_id = item_name_to_id
    location_name_to_id = {}
    # item_name_groups = item_name_groups

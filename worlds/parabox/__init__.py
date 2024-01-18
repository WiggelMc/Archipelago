import logging

from worlds.AutoWorld import World, WebWorld
from worlds.parabox.options import ParaboxOptions
from worlds.parabox.presets import option_presets
from worlds.parabox.groups import item_name_groups

PARABOX_GAME = "Patrick's Parabox"
PARABOX_LOGGER = logging.getLogger(PARABOX_GAME)


class ParaboxWebWorld(WebWorld):
    theme = "ocean"
    options_presets = option_presets


class ParaboxWorld(World):
    """
    Patrick's Parabox is a puzzle game
    that explores a unique recursive system
    of boxes within boxes within boxes within boxes.
    """
    game = PARABOX_GAME
    options_dataclass = ParaboxOptions
    options: ParaboxOptions
    web = ParaboxWebWorld
    topology_present = False

    item_name_to_id = {}
    location_name_to_id = {}
    item_name_groups = item_name_groups

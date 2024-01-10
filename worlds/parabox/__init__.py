from worlds.AutoWorld import World, WebWorld
from worlds.parabox.options import ParaboxOptions

PARABOX_GAME = "Patrick's Parabox"


class ParaboxWebWorld(WebWorld):
    theme = "ocean"


class ParaboxWorld(World):
    """
    Patrick's Parabox is an award-winning puzzle game
    that explores a unique recursive system
    of boxes within boxes within boxes within boxes.
    Learn to manipulate the world's structure
    by pushing boxes into and out of each other.
    Wrap your head around what happens when a box contains itself,
    and learn to use infinity to your advantage.
    Explore many more mechanics and recursive twists
    as you delve deeper and deeper into the system.
    It's boxes all the way down.
    """
    game = PARABOX_GAME
    options_dataclass = ParaboxOptions
    options: ParaboxOptions

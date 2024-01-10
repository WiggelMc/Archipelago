from BaseClasses import Location
from worlds.parabox import PARABOX_GAME


class ParaboxLocation(Location):
    game: str = PARABOX_GAME

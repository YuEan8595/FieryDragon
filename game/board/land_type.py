import enum


class LandType(enum.Enum):
    """
    Enum class to represent the type of land in the game.
    Currently, there are two types of land: Volcano and Cave.
    Dragon can move freely to any volcano if it is not occupied.
    Dragon cannot move to other player's cave.
    """
    VOLCANO = 1
    CAVE = 2

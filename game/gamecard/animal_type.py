import enum


class AnimalType(enum.Enum):
    """
    Enum class to represent the type of animal in the game.
    Animal type that represent reward (allow movement) is put at the front.
    Animal type that represent penalty is put at the back.
    """
    BAT = 0
    BABY_DRAGON = 1
    SALAMANDER = 2
    SPIDER = 3
    DRAGON_PIRATE = 4   # Penalty

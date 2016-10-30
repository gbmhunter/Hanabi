from enum import Enum, unique

# Enumerates the allowed card colors in the Hanabi game
@unique
class Color(Enum):
    blue = 1
    green = 2
    red = 3
    white = 4
    yellow = 5

# Each colour contains cards with these numbers printed on them
# (this also take into account frequency)
numberFreq = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
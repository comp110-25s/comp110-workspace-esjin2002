"""Dictionary thing"""

__author__ = "730469891"


def invert(stuff: dict[str, str]) -> dict[str, str]:
    """Swaps keys and values in a dictionary."""
    flipped: dict[str, str] = dict()
    for key in stuff:
        if stuff[key] in flipped:
            raise KeyError("You're still a failure.")
        flipped[stuff[key]] = key
    return flipped


def count(stuff: list[str]) -> dict[str, int]:
    """Counts the number of times something appears in a list."""
    nums: dict[str, int] = dict()
    for item in stuff:
        if item in nums:
            nums[item] += 1
        else:
            nums[item] = 1
    return nums


def favorite_color(stuff: dict[str, str]) -> str:
    """Finds color that appears most often."""
    colors: dict[str, int] = dict()
    for key in stuff:
        if stuff[key] in colors:
            colors[stuff[key]] += 1
        else:
            colors[stuff[key]] = 1
    fav_color: str = ""
    big: int = 0
    for key in colors:
        if colors[key] > big:
            fav_color = key
            big = colors[key]
    return fav_color


def bin_len(stuff: list[str]) -> dict[int, set]:
    """Organizes words in a list based on number of characters."""
    org: dict[int, set] = dict()
    for word in stuff:
        if len(word) in org:
            org[len(word)].add(word)
        else:
            org[len(word)] = {word}
    return org

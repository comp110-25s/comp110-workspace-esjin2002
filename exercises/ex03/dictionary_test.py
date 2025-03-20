"""Failure"""

__author__ = "730469891"

import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_0() -> None:
    """Tests invert function for error."""
    with pytest.raises(KeyError):
        stuff = {"cena": "john", "cho": "john"}
        invert(stuff)
    return None


def test_invert_1() -> None:
    """Tests invert function normally."""
    assert invert({"A": "B", "C": "D"}) == {"B": "A", "D": "C"}
    return None


def test_invert_2() -> None:
    """Tests invert function normally."""
    assert invert({"You": "Can't", "See": "Me"}) == {"Can't": "You", "Me": "See"}
    return None


def test_invert_3() -> None:
    """Tests invert function with weird case."""
    assert invert({}) == {}
    return None


def test_count_0() -> None:
    """Tests count function normally."""
    assert count(["A", "A", "A", "A", "B", "C"]) == {"A": 4, "B": 1, "C": 1}
    return None


def test_count_1() -> None:
    """Tests count function normally."""
    assert count(["A", "B", "C", "D", "E", "F"]) == {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 1,
        "E": 1,
        "F": 1,
    }
    return None


def test_count_2() -> None:
    """Tests count function with weird case."""
    assert count([]) == {}
    return None


def test_favorite_color_0() -> None:
    """Tests favorite_color function normally."""
    assert (
        favorite_color({"Ken": "Red", "Akuma": "Red", "Bison": "Red", "Ryu": "White"})
        == "Red"
    )
    return None


def test_favorite_color_1() -> None:
    """Tests favorite_color function normally."""
    assert (
        favorite_color({"Ken": "Red", "Akuma": "Red", "Bison": "White", "Ryu": "White"})
        == "Red"
    )
    return None


def test_favorite_color_2() -> None:
    """Tests favorite_color function normally."""
    assert (
        favorite_color({"Ken": "White", "Akuma": "Red", "Bison": "Red", "Ryu": "White"})
        == "White"
    )
    return None


def test_favorite_color_3() -> None:
    """Tests favorite_color function in slightly unusual case."""
    assert (
        favorite_color(
            {"Ken": "Red", "Akuma": "Black", "Bison": "Green", "Ryu": "White"}
        )
        == "Red"
    )
    return None


def test_favorite_color_4() -> None:
    """Tests favorite_color function in weird case."""
    assert favorite_color({"Ken": "4"}) == "4"
    return None


def test_bin_len_0() -> None:
    """Tests bin_len function normally."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
    return None


def test_bin_len_1() -> None:
    """Tests bin_len function normally."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
    return None


def test_bin_len_2() -> None:
    """Tests bin_len function in slightly unusual case."""
    assert bin_len(["the", "the", "the"]) == {3: {"the"}}
    return None


def test_bin_len_3() -> None:
    """Tests bin_len function in weird case."""
    assert bin_len([]) == {}
    return None


def test_bin_len_4() -> None:
    """Tests bin_len function in weird case."""
    assert bin_len(["", "", ""]) == {0: {""}}
    return None

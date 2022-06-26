import pytest

from example import InvalidThrowValue
from example import Player
from example import TooManyThrows


def test_empty_score() -> None:
    player = Player()  # Arrange
    score = player.score()  # Act
    assert score == 0  # Assert


def test_single_round() -> None:
    player = Player()  # Arrange
    player.add_round(2)
    score = player.score()  # Act
    assert score == 2  # Assert


def test_two_rounds() -> None:
    player = Player()  # Arrange
    player.add_round(2)
    player.add_round(3)
    score = player.score()  # Act
    assert score == 5  # Assert


def test_throws_on_zero() -> None:
    player = Player()  # Arrange
    with pytest.raises(InvalidThrowValue):  # Assert
        player.add_round(0)  # Act


def test_throws_on_negative() -> None:
    player = Player()  # Arrange
    with pytest.raises(InvalidThrowValue):  # Assert
        player.add_round(-1)  # Act


def test_zero_throws() -> None:
    player = Player()  # Arrange
    throws = player.throws()  # Act
    assert throws == 0  # Assert


def test_one_throw() -> None:
    player = Player()  # Arrange
    player.add_round(2)
    throws = player.throws()  # Act
    assert throws == 1  # Assert


def test_two_throws() -> None:
    player = Player()  # Arrange
    player.add_round(2)
    player.add_round(3)
    throws = player.throws()  # Act
    assert throws == 2  # Assert


def test_throws_on_nineteen_throws() -> None:
    player = Player()  # Arrange
    for _ in range(18):
        player.add_round(1)

    with pytest.raises(TooManyThrows):  # Assert
        player.add_round(1)

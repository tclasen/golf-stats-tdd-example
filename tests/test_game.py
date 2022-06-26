import pytest

from example import Course
from example import CourseRepository
from example import Game
from example import InMemoryCourseRepository
from example import Player


@pytest.fixture
def course_repository() -> CourseRepository:
    course_repository = InMemoryCourseRepository()
    course_repository.add_course(Course(name="All 4 Example", par=[4] * 18))
    return course_repository


@pytest.fixture
def game_without_course(course_repository: CourseRepository) -> Game:
    player = Player()
    _game = Game(player=player, course_repository=course_repository)
    return _game


@pytest.fixture
def game(game_without_course: Game, course_repository: CourseRepository) -> Game:
    game_without_course.select_course("All 4 Example")
    return game_without_course


def test_user_throw(game: Game) -> None:
    game.add_round(3)
    assert game.score() == ([3], [4] * 18)


@pytest.mark.parametrize(
    "throws",
    [
        [3, 2, 3, 2, 3, 2, 3, 2, 3],
        [2, 2, 2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1],
        [30, 30, 30, 30],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    ],
)
def test_valid_games(game: Game, throws: list[int]) -> None:
    for throw in throws:
        game.add_round(throw)
    assert game.score() == (throws, [4] * 18)


def test_total_score(game: Game) -> None:
    throws = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for throw in throws:
        game.add_round(throw)
    assert game.total_score() == 18


def test_total_score_without_course_crashes(game_without_course: Game) -> None:
    with pytest.raises(ValueError):
        game_without_course.total_score()

from typing import Optional

from example.course import Course
from example.course import CourseRepository
from example.player import Player


class Game:
    def __init__(self, player: Player, course_repository: CourseRepository) -> None:
        self._player = player
        self._course_repository = course_repository
        self._current_course: Optional[Course] = None

    def select_course(self, name: str) -> None:
        self._current_course = self._course_repository.get_course_by_name(name=name)

    def add_round(self, throws: int) -> None:
        if self._current_course is None:
            raise ValueError
        self._player.add_round(throws)

    def score(self) -> tuple[list[int], list[int]]:
        if self._current_course is None:
            raise ValueError
        player = self._player.all_scores()
        course = self._current_course.all_par()
        return (player, course)

    def __len__(self) -> int:
        return len(self._player)

    def total_score(self) -> int:
        if self._current_course is None:
            raise ValueError
        return self._player.score() - self._current_course.par()

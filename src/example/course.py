from __future__ import annotations

from typing import Protocol


class InvalidParValue(ValueError):
    pass


class InvalidParCount(ValueError):
    pass


class CourseRepository(Protocol):
    def get_course_by_name(self, name: str) -> Course:
        ...

    # return Course(name=name, par=[4] * 18)


class Course:
    _min = 3
    _max = 5
    _len = 18

    def __init__(self, name: str, par: list[int]) -> None:
        self._name = name
        self._par = self._validate_par(par)

    @classmethod
    def _validate_par(cls, par: list[int]) -> list[int]:
        if any(i < cls._min for i in par):
            raise InvalidParValue(f"Value below the minimum of {cls._min}")

        if any(i > cls._max for i in par):
            raise InvalidParValue(f"Value above the maximum of {cls._max}")

        if len(par) < cls._len:
            raise InvalidParCount(
                f"Course doesn't have enough holes, needed {cls._len}"
            )

        if len(par) > cls._len:
            raise InvalidParCount(
                f"Course doesn't have enough holes, needed {cls._len}"
            )

        return par

    def __len__(self) -> int:
        return len(self._par)

    def all_par(self) -> list[int]:
        return self._par

    def par(self) -> int:
        return sum(self._par)

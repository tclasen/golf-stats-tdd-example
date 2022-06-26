import pytest

from example import Course
from example import InvalidParCount
from example import InvalidParValue


def test_course_init() -> None:
    par = [4] * 18
    course = Course(name="Example", par=par)

    assert len(course) == 18


def test_course_minimum_par() -> None:
    par = ([4] * 17) + [1]
    with pytest.raises(InvalidParValue):
        Course(name="Example", par=par)


def test_course_maximum_par() -> None:
    par = ([4] * 17) + [8]
    with pytest.raises(InvalidParValue):
        Course(name="Example", par=par)


def test_course_minimum_holes() -> None:
    par = [4] * 17
    with pytest.raises(InvalidParCount):
        Course(name="Example", par=par)


def test_course_maximum_holes() -> None:
    par = [4] * 19
    with pytest.raises(InvalidParCount):
        Course(name="Example", par=par)

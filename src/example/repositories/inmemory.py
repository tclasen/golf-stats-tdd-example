from typing import Optional

from example.course import Course
from example.course import CourseSummary


class InMemoryCourseRepository:
    def __init__(self, courses: Optional[list[Course]] = None) -> None:
        self._courses = courses or []

    def add_course(self, course: Course) -> None:
        self._courses.append(course)

    def get_course_by_name(self, name: str) -> Course:
        for course in self._courses:
            if course._name == name:
                return course
        raise ValueError("Couldn't find course!")

    def get_all_course_names_and_par(self) -> list[CourseSummary]:
        return sorted((i._name, i._par) for i in self._courses)

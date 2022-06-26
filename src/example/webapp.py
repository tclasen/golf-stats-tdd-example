from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import ConstrainedInt
from pydantic import ConstrainedList

from example import Course
from example import InMemoryCourseRepository

app = FastAPI()

DB = InMemoryCourseRepository()
DB.add_course(Course(name="All 4 Example", par=[4] * 18))


class ParCount(ConstrainedList):
    min_items: Optional[int] = 18
    max_items: Optional[int] = 18


class ParValue(ConstrainedInt):
    ge: Optional[int] = 3
    le: Optional[int] = 5


class CourseSummary(BaseModel):
    name: str
    par: ParCount[ParValue]


@app.get("/courses", response_model=list[CourseSummary])
def get_all_courses() -> list[CourseSummary]:
    return [
        CourseSummary(name=name, par=par)
        for name, par in DB.get_all_course_names_and_par()
    ]


@app.post("/courses")
def add_new_course(course: CourseSummary) -> None:
    item = Course(name=course.name, par=course.par)
    print(item)
    DB.add_course(item)

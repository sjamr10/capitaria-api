from typing import Optional

from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    teacher_id: Optional[int]


class CourseCreate(CourseBase):
    pass


class CourseRead(CourseBase):
    id: int

    class Config:
        orm_mode = True


class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentRead(EnrollmentBase):
    id: int

    class Config:
        orm_mode = True


class TestBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    course_id: int


class TestCreate(TestBase):
    pass


class TestRead(TestBase):
    id: int

    class Config:
        orm_mode = True


class GradeBase(BaseModel):
    student_id: int
    test_id: int
    value: float = Field(..., ge=1, le=7)


class GradeCreate(GradeBase):
    pass


class GradeRead(GradeBase):
    id: int

    class Config:
        orm_mode = True

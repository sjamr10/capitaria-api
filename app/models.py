from sqlalchemy import Column, ForeignKey, Integer, Numeric, String

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    name = Column(String(50), nullable=False)


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    name = Column(String(50), nullable=False)


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    test_id = Column(Integer, ForeignKey("tests.id"), nullable=False)
    value = Column(Numeric(2, 1), nullable=False)

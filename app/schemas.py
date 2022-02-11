from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int

    class Config:
        orm_mode = True

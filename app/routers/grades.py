from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Response, status

from app.crud import grades as crud
from app.schemas import GradeCreate, GradeRead

router = APIRouter()

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Grade not found"
)


@router.post("", response_model=GradeRead, status_code=status.HTTP_201_CREATED)
def create(payload: GradeCreate):
    grade = crud.create(payload)
    return grade


@router.get(
    "",
    response_model=List[GradeRead],
)
def get(student_id: Optional[int] = None, sort: str = "student_id:desc"):
    grades = crud.get(sort, student_id)
    return grades


@router.get("/{id}", response_model=GradeRead)
def get_one(id: int = Path(..., gt=0)):
    grade = crud.get_one(id)
    if not grade:
        raise not_found_exception
    return grade


@router.put(
    "/{id}",
    response_model=GradeRead,
)
def update(
    payload: GradeCreate,
    id: int = Path(..., gt=0),
):
    grade = crud.get_one(id)
    if not grade:
        raise not_found_exception
    grade = crud.update(id, payload)
    return grade


@router.delete("/{id}")
def delete(id: int = Path(..., gt=0)):
    grade = crud.get_one(id)
    if not grade:
        raise not_found_exception
    crud.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

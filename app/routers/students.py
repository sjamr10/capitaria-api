from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Response, status

from app.crud import students as crud
from app.schemas import StudentCreate, StudentRead

router = APIRouter()

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
)


@router.post("", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create(payload: StudentCreate):
    student = crud.create(payload)
    return student


@router.get(
    "",
    response_model=List[StudentRead],
)
def get(name: Optional[str] = None, sort: str = "name:desc"):
    students = crud.get(sort, name)
    return students


@router.get("/{id}", response_model=StudentRead)
def get_one(id: int = Path(..., gt=0)):
    student = crud.get_one(id)
    if not student:
        raise not_found_exception
    return student


@router.put(
    "/{id}",
    response_model=StudentRead,
)
def update(
    payload: StudentCreate,
    id: int = Path(..., gt=0),
):
    student = crud.get_one(id)
    if not student:
        raise not_found_exception
    student = crud.update(id, payload)
    return student


@router.delete("/{id}")
def delete(id: int = Path(..., gt=0)):
    student = crud.get_one(id)
    if not student:
        raise not_found_exception
    crud.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

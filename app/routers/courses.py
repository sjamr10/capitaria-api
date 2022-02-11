from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Response, status

from app.crud import courses as crud
from app.schemas import CourseCreate, CourseRead

router = APIRouter()

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
)


@router.post("", response_model=CourseRead, status_code=status.HTTP_201_CREATED)
def create(payload: CourseCreate):
    course = crud.create(payload)
    return course


@router.get(
    "",
    response_model=List[CourseRead],
)
def get(name: Optional[str] = None, sort: str = "name:desc"):
    courses = crud.get(sort, name)
    return courses


@router.get("/{id}", response_model=CourseRead)
def get_one(id: int = Path(..., gt=0)):
    course = crud.get_one(id)
    if not course:
        raise not_found_exception
    return course


@router.put(
    "/{id}",
    response_model=CourseRead,
)
def update(
    payload: CourseCreate,
    id: int = Path(..., gt=0),
):
    course = crud.get_one(id)
    if not course:
        raise not_found_exception
    course = crud.update(id, payload)
    return course


@router.delete("/{id}")
def delete(id: int = Path(..., gt=0)):
    course = crud.get_one(id)
    if not course:
        raise not_found_exception
    crud.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

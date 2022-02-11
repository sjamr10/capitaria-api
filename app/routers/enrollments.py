from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Response, status

from app.crud import enrollments as crud
from app.schemas import EnrollmentCreate, EnrollmentRead

router = APIRouter()

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Enrollment not found"
)


@router.post("", response_model=EnrollmentRead, status_code=status.HTTP_201_CREATED)
def create(payload: EnrollmentCreate):
    enrollment = crud.create(payload)
    return enrollment


@router.get(
    "",
    response_model=List[EnrollmentRead],
)
def get(sort: str = "course_id:desc"):
    enrollments = crud.get(sort)
    return enrollments


@router.get("/{id}", response_model=EnrollmentRead)
def get_one(id: int = Path(..., gt=0)):
    enrollment = crud.get_one(id)
    if not enrollment:
        raise not_found_exception
    return enrollment


@router.put(
    "/{id}",
    response_model=EnrollmentRead,
)
def update(
    payload: EnrollmentCreate,
    id: int = Path(..., gt=0),
):
    enrollment = crud.get_one(id)
    if not enrollment:
        raise not_found_exception
    enrollment = crud.update(id, payload)
    return enrollment


@router.delete("/{id}")
def delete(id: int = Path(..., gt=0)):
    enrollment = crud.get_one(id)
    if not enrollment:
        raise not_found_exception
    crud.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

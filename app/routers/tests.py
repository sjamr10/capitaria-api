from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Response, status

from app.crud import tests as crud
from app.schemas import TestCreate, TestRead

router = APIRouter()

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Test not found"
)


@router.post("", response_model=TestRead, status_code=status.HTTP_201_CREATED)
def create(payload: TestCreate):
    test = crud.create(payload)
    return test


@router.get(
    "",
    response_model=List[TestRead],
)
def get(name: Optional[str] = None, sort: str = "name:desc"):
    tests = crud.get(sort, name)
    return tests


@router.get("/{id}", response_model=TestRead)
def get_one(id: int = Path(..., gt=0)):
    test = crud.get_one(id)
    if not test:
        raise not_found_exception
    return test


@router.put(
    "/{id}",
    response_model=TestRead,
)
def update(
    payload: TestCreate,
    id: int = Path(..., gt=0),
):
    test = crud.get_one(id)
    if not test:
        raise not_found_exception
    test = crud.update(id, payload)
    return test


@router.delete("/{id}")
def delete(id: int = Path(..., gt=0)):
    test = crud.get_one(id)
    if not test:
        raise not_found_exception
    crud.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

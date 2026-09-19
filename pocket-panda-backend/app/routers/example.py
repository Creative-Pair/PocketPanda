from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["example"])
async def read_root():
    return {"message": "Pocket Panda API"}

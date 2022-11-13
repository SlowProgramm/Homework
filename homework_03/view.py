from fastapi import APIRouter

router = APIRouter(
    prefix="/ping"
)

@router.get("")
def show_view():
    return {"message": "pong"}

from fastapi import Depends, APIRouter, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.api.dependencies.database import get_repository
from app.models.user import UserCreate, UserPublic

from app.db.repositories.users import UserRepository


router = APIRouter()


@router.post("/", response_model=UserPublic, name="users:register-new-user", status_code=HTTP_201_CREATED)
async def register_new_user(
    new_user: UserCreate,
    user_repo: UserRepository = Depends(get_repository(UserRepository))
) -> UserPublic:
    created_user = await user_repo.register_new_user(new_user=new_user)
    return created_user

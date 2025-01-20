from fastapi import Depends
from typing import Annotated

from auth.action import get_current_user
import schemas.user as UserSchema

async def protected(current_user: Annotated[UserSchema.Base, Depends(get_current_user)]) -> UserSchema.Base:
    return current_user
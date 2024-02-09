from typing import TYPE_CHECKING, List
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from groot.security import HashedPassword
from pydantic import BaseModel

if TYPE_CHECKING:
    from groot.models.post import Post

class User(SQLModel, table=True):
    "Representa a modelagem do User - User Model"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique =True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword

    # it populates the .user attribute on the Content Model
    posts: List["Post"] = Relationship(back_populates="user")
    
class UserResponse(BaseModel):
    """Serializer for User Response"""

    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None

class UserRequest(BaseModel):
    """"Serializer for User request payload"""
    
    email: str
    username: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None
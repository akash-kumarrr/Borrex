from source.models.base import Base
from source.models.base_model import BaseModel

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(BaseModel):
    __tablename__ = "users"

    email : Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)
    username : Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    fullname : Mapped[str] = mapped_column(String(50), nullable=False)
    hashed_password : Mapped[str] = mapped_column(String(256), nullable=False)
    contact_number : Mapped[str] = mapped_column(String(10), nullable=True)
    status : Mapped[bool] = mapped_column(bool)
from pydantic import EmailStr, BaseModel, Field, ConfigDict, field_validator
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """Base Class for User"""
    email : EmailStr
    username : str
    fullname : str
    contact_number : Optional[str] = Field(..., description="Contact number of user")

    @field_validator("contact_number")
    @classmethod
    def validate_phone(cls, pn):
        if pn is None : return pn
        if not pn.isdigit(): raise ValueError("Phone number should consist of only digits!")
        if len(pn) != 10 :
            raise ValueError("Phone number be of length = 10 digits")
        return pn
    


class UserCreate(UserBase):
    """User create schema for new user during regristration"""
    password : str = Field(..., min_length=6, max_length=25)
    @field_validator("password")
    @classmethod
    def validate_password(cls, p):
        """
            Validate password strength.
        
            Requirements:
            - Minimum 6 characters
            - At least one uppercase letter
            - At least one lowercase letter
            - At least one digit
            - At least one special character (@$!%*?&)
        """

class UserLoginViaEmail(BaseModel):
    """User login schema"""
    email : EmailStr
    password : str

class UserLoginViaUsername(BaseModel):
    """User Login Schema"""
    username : str
    password : str


class UserCreateResponse(BaseModel):
    id : str
    email : EmailStr
    username : str
    fullname : str
    created_at : datetime
    updated_at : datetime

class TokenResponse(BaseModel):
    access_token : str
    token_type : str = "Bearer"
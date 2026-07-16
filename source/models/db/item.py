from typing import List, Dict, Any
from sqlalchemy import String, Enum as SQLEnum, JSON
from sqlalchemy.orm import Mapped, mapped_column
from source.models.base_model import BaseModel
from source.models.schemas.item import *

class Item(BaseModel):
    __tablename__ = "items"
    
    owner_id: Mapped[str] = mapped_column(String, index=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(2000))
    category: Mapped[str] = mapped_column(String)
    
    images: Mapped[List[str]] = mapped_column(JSON)                  # List of URLs
    tags: Mapped[List[str]] = mapped_column(JSON, default=list)       
    specifications: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict) 

    condition: Mapped[ItemCondition] = mapped_column(
        SQLEnum(ItemCondition), default=ItemCondition.GOOD
    )
    status: Mapped[ItemStatus] = mapped_column(
        SQLEnum(ItemStatus), default=ItemStatus.AVAILABLE
    )
    verification_status: Mapped[VerificationStatus] = mapped_column(
        SQLEnum(VerificationStatus), default=VerificationStatus.PENDING
    )

    pricing: Mapped[Dict[str, Any]] = mapped_column(JSON)
    location: Mapped[Dict[str, Any]] = mapped_column(JSON)
    metrics: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)
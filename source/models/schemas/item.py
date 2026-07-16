from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, HttpUrl, field_validator
from datetime import datetime

class ItemStatus(str, Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    ACTIVE_LOAN = "active_loan"
    MAINTENANCE = "maintenance"
    HIDDEN = "hidden"


class ItemCondition(str, Enum):
    NEW = "New"
    LIKE_NEW = "Like New"
    GOOD = "Good"
    FAIR = "Fair"


class VerificationStatus(str, Enum):
    PENDING = "pending"
    VERIFIED = "verified"
    REJECTED = "rejected"


class LocationModel(BaseModel):
    type: str = "Point"
    coordinates: List[float] = Field(..., min_length=2, max_length=2)  # [longitude, latitude]
    fuzzyLocation: str = Field(..., description="Neighborhood or city level location")
    postalCode: str = Field(..., pattern=r"^\d{5}(-\d{4})?$|^[A-Z\d]{3,8}$")

    @field_validator("coordinates")
    @classmethod
    def validate_coordinates(cls, coords: List[float]) -> List[float]:
        lon, lat = coords
        if not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
            raise ValueError("Coordinates must be valid GPS Longitude/Latitude values")
        return coords


class PricingModel(BaseModel):
    dailyRate: int = Field(..., gt=0, description="Rate in cents (e.g., 1500 = $15.00)")
    weeklyRate: Optional[int] = Field(None, gt=0)
    securityDeposit: int = Field(0, ge=0)
    currency: str = Field("USD", max_length=3)
    minimumRentalDays: int = Field(1, ge=1)


class MetricsModel(BaseModel):
    averageRating: float = Field(0.0, ge=0.0, le=5.0)
    reviewCount: int = Field(0, ge=0)
    totalLends: int = Field(0, ge=0)


class ItemBase(BaseModel):
    """
    Pure Pydantic model for data validation.
    No framework dependencies, no manual ID handling.
    """
    ownerId: str
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=2000)
    images: List[HttpUrl]
    category: str
    tags: List[str] = Field(default_factory=list)
    specifications: Dict[str, str | int | float] = Field(default_factory=dict)
    
    condition: ItemCondition = ItemCondition.GOOD
    status: ItemStatus = ItemStatus.AVAILABLE
    verificationStatus: VerificationStatus = VerificationStatus.PENDING
    
    pricing: PricingModel
    location: LocationModel
    metrics: MetricsModel = Field(default_factory=MetricsModel)

class ItemCreateResponse(BaseModel):
    id : str
    title : str
    status : ItemStatus
    created_at : datetime
    updated_at : datetime
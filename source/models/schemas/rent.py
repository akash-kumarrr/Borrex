









from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self

class RentBase(BaseModel):
    """
    Schema for any Asset for rent
    """
    from_userid: str
    to_userid: str
    asset_id: str
    borrow_time: int = Field(..., description="Number of hours it's been renting...")
    hourly_rate: int = Field(..., description="Price per hour in cents")
    is_active : bool = Field(..., default=True)


class RentCreate(RentBase): 
    total_charge: int = Field(0, description="Renting Hours * Hourly Rate (automatically calculated)")
    @model_validator(mode="after")
    def calculate_total_charge(self) -> Self:
        self.total_charge = self.borrow_time * self.hourly_rate
        return self
    
 
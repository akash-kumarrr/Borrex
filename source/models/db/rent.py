from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from source.models.base_model import BaseModel

class Rent(BaseModel):
    __tablename__ = "rents"

    # --- Foreign Keys / User IDs ---
    from_userid: Mapped[str] = mapped_column(String, index=True)
    to_userid: Mapped[str] = mapped_column(String, index=True)
    asset_id: Mapped[str] = mapped_column(String, index=True)
    
    # --- Rental Duration & Pricing (In Cents) ---
    rent_time: Mapped[int] = mapped_column(Integer)          # Hours
    hourly_rate: Mapped[int] = mapped_column(Integer)        # In cents (e.g. 500 = $5.00)
    total_charge: Mapped[int] = mapped_column(Integer)       # Rent_time * Hourly_rate (stored in DB)
    
    # --- Status ---
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
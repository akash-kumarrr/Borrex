from source.repository.base_repository import BaseRepository
from source.models.db.rent import Rent

class RentRepositoru(BaseException[Rent]):
    def __init__(self, db):
        super().__init__(db, Rent)
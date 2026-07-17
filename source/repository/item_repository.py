from source.repository.base_repository import BaseRepository
from source.models.db.item import Item

class ItemRepository(BaseRepository[Item]):
    def __init__(self, db):
        super().__init__(db, Item)


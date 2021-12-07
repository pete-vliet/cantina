from sqlalchemy import Column, Integer, String
from api.db import Base

class CollectionItem(Base):
    __tablename__ = 'collection_items'
    id = Column(Integer, primary_key=True)
    title = Column(String(120))
    main_artist = Column(String(120))
    genre = Column(String(50))
    image_url = Column(String(225))

    def __init__(self, title=None, main_artist=None, genre=None, image_url=None):
        self.title = title
        self.main_artist = main_artist
        self.genre = genre
        self.image_url = image_url

    def __repr__(self):
        return f'<CollectionItem {self.title!r} by {self.main_artist!r}>'

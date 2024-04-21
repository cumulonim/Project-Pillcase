from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from resources import db

class PillModel(db.Model):
    __tablename__ = 'pills'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    grid: Mapped[int] = mapped_column(Integer, nullable=False, unique=False)
    piece: Mapped[int] = mapped_column(Integer, nullable=False)
    time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'grid': self.grid,
            'piece': self.piece,
            'time': self.time.isoformat()

        }


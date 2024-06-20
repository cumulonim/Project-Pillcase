from sqlalchemy import Select, asc, and_
from datetime import datetime

from models.pillm import PillModel
from resources import db


class PillService:
    def get_pill_by_id(self, pill_id: int):
        return db.session.get(PillModel, pill_id)

    def get_all_pills(self):
        query = Select(PillModel).order_by(asc(PillModel.grid))
        return db.session.scalars(query).all()

    def get_pill_by_grid(self, pill_grid: str):
        query = Select(PillModel).where(PillModel.grid == pill_grid)
        return db.session.scalars(query).all()

    def find_pills_by_time_range(self, start_time: datetime, end_time: datetime):
        pills = PillModel.query.filter(
            and_(PillModel.time >= start_time, PillModel.time <= end_time)
        ).all()
        
        return pills
    def create_pill(self, pill_model: PillModel):
        # exist_pills = self.get_pill_by_grid(pill_model.grid)
        # if exist_pills:
        #     raise Exception(f'Pill exists with grid "{pill_model.grid}"')

        db.session.add(pill_model)
        db.session.commit()

        return pill_model

    # def update_pill(self, pill_model: PillModel):
    #     exist_pill = self.get_pill_by_id(pill_model.id)
    #     if not exist_pill:
    #         raise Exception(f'Pill not found with id: {pill_model.id}')

    #     if pill_model.grid:
    #         exist_pill.grid = pill_model.grid
    #     if pill_model.piece:
    #         exist_pill.piece = pill_model.piece
    #     if pill_model.time:
    #         exist_pill.time = pill_model.time

    #     db.session.commit()

    #     return exist_pill
    def update_pill(self, pill_id: int, **kwargs):
        exist_pill = self.get_pill_by_id(pill_id)
        if not exist_pill:
            raise Exception(f'Pill not found with id: {pill_id}')

        for key, value in kwargs.items():
            if hasattr(exist_pill, key) and value is not None:  
                setattr(exist_pill, key, value)

        db.session.commit()

        return exist_pill
    
    def delete_pill_by_id(self, pill_id: int):
        pill = PillModel.query.get(pill_id)
        if pill:
            db.session.delete(pill)
            db.session.commit()
            return True
        else:
            return False
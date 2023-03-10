from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from v1.vehicles.models.vehicle import Vehicle 

class VehicleDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_vehicle(self, model: str, license_number: str,   reserved: bool):
        new_vehicle = Vehicle(model=model,license_number=license_number, reserved=reserved)
        self.db_session.add(new_vehicle)
        await self.db_session.flush()

    async def get_all_vehicles(self) -> List[Vehicle]:
        q = await self.db_session.execute(select(Vehicle).order_by(Vehicle.id))
        return q.scalars().all()

    async def update_vehicle(self, vehicle_id: int, model: Optional[str], license_number: Optional[str], reserved: Optional[bool]):
        q = update(Vehicle).where(Vehicle.id == vehicle_id)
        if model:
            q = q.values(model=model)
        if license_number:
            q = q.values(license_number=license_number)
        if reserved:
            q = q.values(reserved=reserved)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)

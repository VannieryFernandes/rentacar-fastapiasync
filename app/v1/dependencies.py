from v1.db.config import async_session
from v1.vehicles.controllers.vehicle_dal import VehicleDAL


async def get_vehicle_dal():
    async with async_session() as session:
        async with session.begin():
            yield VehicleDAL(session)
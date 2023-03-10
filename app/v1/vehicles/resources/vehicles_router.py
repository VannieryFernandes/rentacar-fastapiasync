from typing import List, Optional

from fastapi import APIRouter, Depends

from v1.vehicles.controllers.vehicle_dal import VehicleDAL
from v1.vehicles.models.vehicle import Vehicle
from v1.dependencies import get_vehicle_dal

router = APIRouter()


@router.post("/vehicles")
async def create_vehicle(model: str, license_number: str, reserved: bool, vehicle_dal: VehicleDAL = Depends(get_vehicle_dal)):
    return await vehicle_dal.create_vehicle(model, license_number, reserved)


@router.put("/vehicles/{vehicle_id}")
async def update_vehicle(vehicle_id: int, model: Optional[str] = None, license_number: Optional[str] = None, reserved: Optional[bool] = None,
                      vehicle_dal: VehicleDAL = Depends(get_vehicle_dal)):
    return await vehicle_dal.update_vehicle(vehicle_id, model, license_number, reserved)


@router.get("/vehicles", response_model=None)
async def get_all_vehicles(vehicle_dal: VehicleDAL = Depends(get_vehicle_dal)) -> List[Vehicle]:
    return await vehicle_dal.get_all_vehicles()

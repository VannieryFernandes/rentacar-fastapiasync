import uvicorn
from fastapi import FastAPI

from v1.db.config import engine, Base
from v1.vehicles.resources import vehicles_router

app = FastAPI(title="Rent a car")
app.include_router(vehicles_router.router)


@app.on_event("startup")
async def startup():
    print("Started api")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1')

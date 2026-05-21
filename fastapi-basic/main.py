from cross_inertia.fastapi import InertiaDep
from cross_inertia.fastapi.experimental import inertia_lifespan
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(lifespan=inertia_lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(inertia: InertiaDep):
    return inertia.render("Home", {"message": "Hello from Cross-Inertia!"})

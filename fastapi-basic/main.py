from cross_inertia.fastapi import InertiaDep
from cross_inertia.fastapi.experimental import inertia_lifespan
from fastapi import FastAPI

app = FastAPI(lifespan=inertia_lifespan)
app.frontend("/static", directory="static", fallback=None)


@app.get("/")
async def home(inertia: InertiaDep):
    return inertia.render("Home", {"message": "Hello from Cross-Inertia!"})

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functions.surface import surfaceFct

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# run 'make dev' to test the application


@app.get("/")
def welcome():
    return {"message": "Welcome to Jina Fast API"}


# BaseModel for surfaceFct params
class SurfaceParams(BaseModel):
    list_des_x: list
    list_des_y: list


@app.post("/fct/surface/api")
def surface(params: SurfaceParams):
    s = surfaceFct(params.list_des_x, params.list_des_y)
    return {"La surface": s}


@app.get("/fct/surface/api")
def surface():
    return {"message": "Welcome to Surface Function API"}


@app.get("/fct/surface", response_class=HTMLResponse)
async def surface_page(request: Request):
    return templates.TemplateResponse("surface.html", {"request": request})

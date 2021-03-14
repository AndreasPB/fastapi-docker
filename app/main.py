import fastapi
from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse
from jinja2 import Environment, FileSystemLoader


app = FastAPI()

some_file_path = "media/img/bg_clouds.jpg"

templates = Jinja2Templates(directory="app/templates")



@app.get('/')
async def index():
    return {'message': 'heyo'}

@app.get('/home')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        'request': request
        })
  
@app.get('/bg')
async def background():
    return FileResponse(some_file_path)
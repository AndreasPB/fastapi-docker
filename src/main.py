import fastapi
from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse
from jinja2 import Environment, FileSystemLoader


app = FastAPI()

templates = Jinja2Templates(directory='src/templates')


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request
        })

@app.get('/msg')
async def index():
    return {'message': 'heyo'}
  
@app.get('/img')
async def image():
    return FileResponse('src/media/img/bg_clouds.jpg')
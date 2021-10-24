from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def something(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/inputs")
async def inputdata():
    return templates.TemplateResponse("input.html")

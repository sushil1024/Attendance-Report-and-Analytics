from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def something(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/login/{username}")
def authent(username: str, password: str):
    if username == "root" and password == "root":
        return "Access Granted"

        @app.post("/inputs")
        async def inputdata(request: Request, rollno: int):
            return templates.TemplateResponse("input.html", {"request": Request, "StudentRollNo": rollno})

    else:
        return "Inavlid Credentials"



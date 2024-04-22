from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import yagmail
from models import Formulario, EmailStr
from dotenv import load_dotenv
import os
#Cargar variables de entorno
load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/form/")
async def send_email(nombre: str = Form(...), subject: str = Form(...), telefono: str = Form(...), mensaje: str = Form(...)):
    yag = yagmail.SMTP(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))
    email = "gabrielcabreraromo2019@gmail.com"
    to = email
    subject = subject
    body = f"Name: {nombre}\nPhone: {telefono}\nMessage: {mensaje}"
    yag.send(to, subject, body)
    return RedirectResponse(url="/?message=email_sent", status_code=303)



from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from .convert import convert_image

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert(
    file: UploadFile = File(...),
    input_format: str = Form(...),
    format: str = Form(...)
):
    # Save uploaded file
    input_path = f"uploads/{file.filename}"
    output_path = f"outputs/{os.path.splitext(file.filename)[0]}.{format}"
    
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    
    with open(input_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    success, result = convert_image(input_path, output_path, input_format, format)
    
    if success:
        return {"success": True, "output_path": result}
    else:
        return {"success": False, "error": result}

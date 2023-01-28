from fastapi import FastAPI, UploadFile, HTTPException, status
from fastapi.responses import FileResponse
from processing.generator import html_to_docx
import pypandoc
from pathlib import Path

app = FastAPI(title="Converter Engine")


@app.post("/engine")
async def converter(form : str):
    form = form
    # print(f"{file}.html")
    # input = Path(file)
    res = pypandoc.convert_file("example.html", "rst")
    assert res == "berhasil"

    # if not html_file:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    # saved = f"saved/{form}"
    
    # return FileResponse(path=f"{saved}.docx", filename=f"{form}.docx")

import pypandoc
from fastapi import UploadFile

async def html_to_docx(file=str):
    res = pypandoc.convert_file(source = f"py-converter-engine/example.docx", format="html", to="docx")
    assert res == "berhasil"

def halo():
    print("halo")
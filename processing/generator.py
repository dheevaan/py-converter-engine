from bs4 import BeautifulSoup

async def html_to_docx():
    
    with open("./processing/example2.html", "r") as f:
        contens = f.read()
        
        soup = str(BeautifulSoup(contens, "lxml"))
        return soup

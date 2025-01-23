import pymupdf
import os

def resume_parsing(file):
    doc = pymupdf.open(file)
    file_name = os.path.basename(file)
    root_ext = os.path.splitext(file_name)
    name = root_ext[0]
    name += '.txt'
    out = open(f'/Users/aparimeyatiwari/Downloads/MSQ_Bot_Podcast/flask_code/json/{name}','wb')

    for page in doc:
        text = page.get_text().encode("utf8")
        out.write(text)

    out.close()


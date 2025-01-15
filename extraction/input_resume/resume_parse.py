import pymupdf

doc = pymupdf.open("richa_resume.pdf")
out = open("output_resume1.txt","wb")

for page in doc:
    text = page.get_text().encode("utf8")
    out.write(text)

out.close()
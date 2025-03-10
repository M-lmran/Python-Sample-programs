



from PyPDF2 import PdfReader, PdfWriter
with open("Tajudeen_CV.pdf", "rb") as file:
    reader = PdfReader(file)
    page = reader.pages[0]
    page.rotate(90)
    writer = PdfWriter()
    writer.add_page(page)
    with open("updated_cv.pdf", "wb") as new:
        writer.write(new)
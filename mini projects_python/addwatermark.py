import PyPDF2
file_1 = PyPDF2.PdfReader(open("Tajudeen_CV.pdf", "rb"))
to_watermark = PyPDF2.PdfReader(open("watermark_watermark.pdf", "rb"))
output = PyPDF2.PdfWriter()
for i in range(len(file_1.pages)):
    page = file_1.pages[i]
    page.merge_page(to_watermark.pages[0])
    output.add_page(page)
    with open("merged_watermark.pdf", "wb") as final:
        output.write(final)

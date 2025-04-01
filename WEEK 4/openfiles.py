# import PyPDF2

# # Open the PDF file in binary read mode
# file = open("javascript-basics.pdf", "rb")
# reader = PyPDF2.PdfReader(file)
# for page in reader.pages:
#     print(page.extract_text())


file = open("automata.docx", "r")
data = file.read()

print(data)

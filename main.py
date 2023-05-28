from fpdf import FPDF
import os

# Get the list of all files and directories
file_path = "files"
file_list = os.listdir(file_path)

print("Files and directories in '", file_path, "' :")

# prints all files
print(file_list)

pdf = FPDF(orientation="P", unit="mm", format="A4")

for file in file_list:
    title = file.strip(".txt")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", size=20)
    pdf.cell(w=0, h=10, txt=f"{title.capitalize()}", border=0, ln=1)

    pdf.set_font("Helvetica", size=12)
    with open(f"files/{file}") as text_file:
        content = text_file.read()  # first line is title

    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")

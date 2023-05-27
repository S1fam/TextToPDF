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
        lines = text_file.readlines()  # first line is title

    for line in lines:
        words = line.strip().split(" ")
        current_x = pdf.get_x()

        for word in words:
            word_width = pdf.get_string_width(s=word)

            if (current_x + word_width) > 200:
                pdf.ln()
                pdf.set_x(10)

            pdf.cell(word_width + 1, h=5, txt=word, ln=0)

            current_x = pdf.get_x() + word_width

        pdf.ln()

pdf.output("output.pdf")

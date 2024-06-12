import os
import sys
from pylatex import Document, NoEscape

def compile_latex_file(input_path: str) -> str:
    """
    Compile a LaTeX file to a PDF.
    """
    if not os.path.exists(input_path):
        print(f"File {input_path} does not exist.")
        return ""

    with open(input_path, 'r') as file:
        latex_content = file.read()

    doc = Document()

    doc.append(NoEscape(latex_content))

    output_path = os.path.splitext(input_path)[0]
    try:
        doc.generate_pdf(output_path, clean_tex=False)
        print(f"PDF successfully created: {output_path}.pdf")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

    if output_path == "":
        return ""
    else:
        return f"{output_path}.pdf"

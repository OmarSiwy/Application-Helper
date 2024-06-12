import PyPDF2
from typing import Union

def append_pdfs(pdf1_path: str, pdf2_path: str, output_path: str) -> None:
    """
    Append two PDFs together and save the resulting path.
    """
    try:
        pdf1 = PyPDF2.PdfFileReader(pdf1_path)
        pdf2 = PyPDF2.PdfFileReader(pdf2_path)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Append pages from the first PDF
        for page_num in range(pdf1.getNumPages()):
            page = pdf1.getPage(page_num)
            pdf_writer.addPage(page)

        # Append pages from the second PDF
        for page_num in range(pdf2.getNumPages()):
            page = pdf2.getPage(page_num)
            pdf_writer.addPage(page)

        # Write out the combined PDF
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"PDFs successfully appended and saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred while appending PDFs: {e}")

def read_tex(tex_file_path: str) -> str:
    """
    Read the content of a .tex file.
    """
    try:
        with open(tex_file_path, 'r') as file:
            content = file.read()
        print(f"Successfully read .tex file from: {tex_file_path}")
        return content
    except Exception as e:
        print(f"An error occurred while reading the .tex file: {e}")
        return ""

def write_tex(tex_file_path: str, content: str) -> None:
    """
    Write content to a .tex file.
    """
    try:
        with open(tex_file_path, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to .tex file at: {tex_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the .tex file: {e}")

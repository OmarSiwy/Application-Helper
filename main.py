import subprocess
import PyPDF2
import os

def compile_latex_to_pdf(latex_file):
    """
    Compile a LaTeX file into a PDF using pdflatex.
    """
    try:
        # Compile the LaTeX file to PDF
        subprocess.run(['pdflatex', latex_file], check=True)
        # Get the name of the output PDF
        pdf_file = latex_file.replace('.tex', '.pdf')
        return pdf_file
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LaTeX file: {e}")
        return None

def append_pdf(input_pdf, output_pdf):
    """
    Append a PDF file to another PDF file.
    """
    try:
        # Create a PDF reader and writer
        reader_input = PyPDF2.PdfFileReader(input_pdf)
        reader_output = PyPDF2.PdfFileReader(output_pdf)
        writer = PyPDF2.PdfFileWriter()

        # Add all pages from the original output PDF
        for page_num in range(reader_output.getNumPages()):
            page = reader_output.getPage(page_num)
            writer.addPage(page)

        # Add all pages from the new input PDF
        for page_num in range(reader_input.getNumPages()):
            page = reader_input.getPage(page_num)
            writer.addPage(page)

        # Write the combined PDF to a new file
        combined_pdf = 'combined_output.pdf'
        with open(combined_pdf, 'wb') as out_file:
            writer.write(out_file)

        return combined_pdf
    except Exception as e:
        print(f"Error appending PDFs: {e}")
        return None

def main(latex_file, output_pdf):
    # Compile the LaTeX file to PDF
    compiled_pdf = compile_latex_to_pdf(latex_file)
    if not compiled_pdf:
        print("Failed to compile LaTeX file.")
        return

    # Append the compiled PDF to the existing output PDF
    combined_pdf = append_pdf(compiled_pdf, output_pdf)
    if not combined_pdf:
        print("Failed to append PDFs.")
        return

    print(f"Successfully created combined PDF: {combined_pdf}")

if __name__ == "__main__":
    latex_file = "your_latex_file.tex"  # Replace with your LaTeX file name
    output_pdf = "existing_output.pdf"  # Replace with the existing PDF file name
    main(latex_file, output_pdf)


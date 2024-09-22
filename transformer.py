import pdf2image

def convert_pdf_to_png(pdf_path, output_folder):
    """Converts each page of a PDF to a PNG image."""

    images = pdf2image.convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image.save(f"{output_folder}/page_{i+1}.png")

if __name__ == "__main__":
    pdf_path = "Almanac_issue_51.pdf"  # Replace with the path to your PDF
    output_folder = "output_images"  # Replace with your desired output folder

    convert_pdf_to_png(pdf_path, output_folder)
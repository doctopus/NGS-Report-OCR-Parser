import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path

# Path to the input and output folders
input_folder = 'data/input'  # Replace with the actual input folder path
output_folder = 'data/output'  # Replace with the actual output folder path

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# Function to extract text from different file formats using Tesseract OCR
def extract_text(file_path):
    # Extract the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Extract text from image files (JPEG, PNG)
    if file_extension in ['.jpeg', '.jpg', '.png']:
        # Open the image file using PIL
        image = Image.open(file_path)

        # Convert the image to grayscale
        grayscale_image = image.convert('L')

        # Extract text from the image using Tesseract OCR
        extracted_text = pytesseract.image_to_string(grayscale_image)

        return extracted_text

    # Extract text from PDF
    elif file_extension == '.pdf':
        # Convert PDF pages to images using pdf2image
        pages = convert_pdf_to_images(file_path)

        # Variable to store extracted text
        extracted_text = ''

        # Iterate over each page image and extract text using Tesseract OCR
        for page_image in pages:
            # Convert PIL image to grayscale
            image = page_image.convert('L')

            # Extract text from the image using Tesseract OCR
            text = pytesseract.image_to_string(image)

            # Append extracted text to the result
            extracted_text += text

        return extracted_text

    else:
        raise ValueError("Unsupported file format")


# Function to convert PDF pages to images using pdf2image
def convert_pdf_to_images(pdf_path):
    # from pdf2image import convert_from_path

    # Convert PDF pages to PIL images
    pages = convert_from_path(pdf_path)

    return pages


# Iterate over each file in the input folder
for file_name in os.listdir(input_folder):
    # Skip .DS_Store file
    if file_name == '.DS_Store':
        continue
    file_path = os.path.join(input_folder, file_name)

    # Extract text from the file
    try:
        result_text = extract_text(file_path)

        # Write the extracted text to a file in the output folder
        output_file_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.txt')
        with open(output_file_path, 'w') as output_file:
            output_file.write(result_text)

        print(f"Text extracted from '{file_name}' and saved to '{output_file_path}'")

    except ValueError as e:
        print(f"Error processing '{file_name}': {str(e)}")

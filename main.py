import os
from pdf_processing import extract_tables_from_pdf, process_tables
from image_processing import process_image
import json

# Define Input and Output Directories
input_directory = 'data/input'
output_directory = 'data/output'


def process_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        tables = extract_tables_from_pdf(file_path)
        processed_tables = process_tables(tables)
        # Do further processing or saving as JSON
        # output_file_name = f"{os.path.basename(file_path)}.json" #For including the file extension
        output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.json'
        output_file_path = os.path.join(output_directory, output_file_name)
        with open(output_file_path, 'w') as output_file:
            json.dump(processed_tables, output_file)
        print(f"Processed file: {file_path}")

    elif file_extension in ['.jpg', '.jpeg', '.png']:
        # output_file_name = f"{os.path.basename(file_path)}.json" #For including the file extension
        output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.json'
        output_file_path = os.path.join(output_directory, output_file_name)
        process_image(file_path, output_file_path)
        # Do further processing or saving as JSON
        print(f"Processed file: {file_path}")

    else:
        print(f"Unsupported file format: {file_extension}")


def process_files_in_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            process_file(file_path)


# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process files in the input directory
process_files_in_directory(input_directory)

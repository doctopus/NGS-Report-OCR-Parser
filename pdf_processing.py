import camelot


def extract_tables_from_pdf(pdf_path):
    tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')
    return tables


def process_tables(tables):
    # Process the tables data as needed
    processed_tables = []
    for table in tables:
        # Perform data extraction, cleaning, etc.
        processed_table = extract_data_from_table(table)
        processed_tables.append(processed_table)
    return processed_tables


def extract_data_from_table(table):
    # Extract data from table and return as desired format
    # Example: Extract table data as a list of lists
    data = []
    for row in table.df.itertuples(index=False):
        data.append(list(row))
    return data


def process_pdf(pdf_path):
    tables = extract_tables_from_pdf(pdf_path)
    processed_tables = []

    if isinstance(tables, camelot.core.TableList):
        for table in tables:
            processed_table = process_single_table(table)
            processed_tables.append(processed_table)
    else:
        processed_tables = process_single_table(tables)

    # Do further processing or saving as JSON
    return processed_tables


def process_single_table(table):
    # Process a single table and return the result
    processed_table = {}
    # Perform data extraction, cleaning, etc.
    # ...
    return processed_table


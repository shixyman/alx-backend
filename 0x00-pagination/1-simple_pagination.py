import csv
from typing import List, Dict, Any, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

def get_page(page: int = 1, page_size: int = 10) -> List[Dict[str, Any]]:
    assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0."
    assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

    dataset = []  # List to store the dataset

    # Read the CSV file and populate the dataset list
    with open('your_csv_file.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        dataset = list(csv_reader)

    start_index, end_index = index_range(page, page_size)
    if start_index >= len(dataset):
        return []  # Return an empty list if the start index is out of range

    return dataset[start_index:end_index]
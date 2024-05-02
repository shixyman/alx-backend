import math

def get_hyper(page: int = 1, page_size: int = 10) -> Dict[str, Any]:
    assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0."
    assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

    dataset = get_page(page, page_size)  # Retrieve the dataset page using the get_page method

    page_length = len(dataset)
    total_pages = math.ceil(len(dataset) / page_size)

    next_page = page + 1 if page < total_pages else None
    prev_page = page - 1 if page > 1 else None

    return {
        'page_size': page_length,
        'page': page,
        'data': dataset,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages
    }

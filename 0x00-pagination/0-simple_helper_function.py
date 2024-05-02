#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page, page_size)-> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index

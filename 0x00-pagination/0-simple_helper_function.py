#!/usr/bin/env python3
"""
Generates start and end index given pagination parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Generates start and end index given pagination parameters

    Parameters
    page : int
        The page number
    page_size: int
        The size of the page

    Return : int
        Start and end index
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)

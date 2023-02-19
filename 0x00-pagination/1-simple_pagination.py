#!/usr/bin/env python3
"""
Server class to paginate a database of popular baby names.
A method that calculates the index is also included
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init method for class server"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Given the paging parameters retrieves the correct document

        Parameters
            page : int
                The page number
            page_size: int
                The size of the page

        Return : List[List]
            A list of the required documents
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        dataset = self.dataset()

        # Getting the indexes
        start, end = index_range(page, page_size)

        # Checking if the index is out of range
        if start > len(dataset) or end > len(dataset):
            return []

        # Retrieving the documents
        return(dataset[start:end])

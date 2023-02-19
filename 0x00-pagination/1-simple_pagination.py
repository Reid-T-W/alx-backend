#!/usr/bin/env python3


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
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        # if page > len(dataset) or page_size > len(dataset):
        #     return []
        # Getting the page
        start, end = index_range(page, page_size)
        if start > len(dataset) or end > len(dataset):
            # print(f"Length {len(dataset )}, start {start}, end {end}")
            return []
        return(dataset[start:end])

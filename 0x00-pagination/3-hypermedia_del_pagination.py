#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializing some variables
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str,
                                                     Union[int, List[List]]]:
        """
        Handles pagination in cases were data is deleted in between queries.
        Numerical indexes that are assigned as keys to every row of the data
        are made use of.

        Parameters
            index: the current index
            page_size: size of a single page
        Return
            A dictionary containing the data, current  index,
            page_size and next_index
        """
        assert index < len(self.__indexed_dataset)
        assert page_size < len(self.__indexed_dataset)
        keys = list(self.__indexed_dataset.keys())
        corrected_index = index
        # The while loop below handles cases where a deleted index is
        # encountred. It iterates until it finds the next index that is
        # not deleted
        while (corrected_index not in keys) and (corrected_index <
                                                 len(self.__indexed_dataset)):
            corrected_index += 1
        next_index = corrected_index + page_size
        indexs = [i for i in range(corrected_index, next_index)]
        data = [self.__indexed_dataset[index] for index in indexs]
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }

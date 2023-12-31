#!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    return (page - 1) * page_size, page * page_size


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
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        startidx, endidx = index_range(page, page_size)

        try:
            data = self.dataset()[startidx: endidx]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data = self.get_page(page, page_size)
        total_page = len(self.dataset()) // page_size + 1
        return {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "data": data,
            "next_page": page + 1 if page + 1 <= total_page else None,
            "prev_page": page - 1 if page - 1 > 1 else None,
            "total_page": total_page
        }
    

    def get_hyper_index():
        

    


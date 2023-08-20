import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return index of start and end base on page and page_size
    Args:
        page (int) - the current page the user is on
        page_size (int) - the number of items per page
    Return:
        tuple(startindex, endindex)
    """
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
        """
        get the page and page_size and paginate the dataset base on the args
        Args:
            page (int) - the current page the user is on
            page_size (int) - the number of items per page
        Return:
            List[List]
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        try:
            return self.dataset()[start: end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            List[List]: The page of the dataset.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        return ({
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "data": data,
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        })

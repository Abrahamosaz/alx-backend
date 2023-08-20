#!/usr/bin/env python3
import math
from typing import Tuple
"""
function that return a tuple of start and end index for the
pagination of the data
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return index of start and end base on page and page_size
    """
    return (page - 1) * page_size, page * page_size

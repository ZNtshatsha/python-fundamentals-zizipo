
import numpy as np

from src.userzizi_timing import measure_time


@measure_time
def multiply_with_list(lst: list[int], scalar: int) -> list[int]:
    return [x * scalar for x in lst]


@measure_time
def multiply_with_numpy(arr: np.ndarray, scalar: int) -> np.ndarray:
    return arr * scalar

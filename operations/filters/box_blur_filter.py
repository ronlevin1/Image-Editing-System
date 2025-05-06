import numpy as np

from core.convolver import Convolver
from core.image_data import ImageData
from operations.base.filter_decorator import FilterDecorator


class BoxBlurFilter(FilterDecorator):
    """
    Concrete decorator for box blur filter using the Decorator pattern.
    """
    def __init__(self, width: int, height: int, next_filter=None):
        super().__init__(next_filter)
        # TODO: change accepted range
        self.width = width
        self.height = height
        # normalized box kernel
        self.kernel = np.ones((height, width), dtype=float) / (width * height)

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        # extract raw array
        arr = image_data.get_array()
        blurred = Convolver.apply_kernel(arr, self.kernel)
        # update and return
        image_data.image = blurred
        return image_data
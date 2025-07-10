import numpy as np

from core.convolver import Convolver
from core.image_data import ImageData
from operations.base.filter_decorator import FilterDecorator

class BoxBlurFilter(FilterDecorator):
    """
    Concrete decorator for box blur filter using the Decorator pattern.
    """
    def __init__(self, width: int, height: int, wrapped_operation=None):
        super().__init__(wrapped_operation)
        # self.width = width
        # self.height = height
        # accepted range
        self.width = max(3, min(31, width if width % 2 == 1 else width + 1))
        self.height = max(3, min(31, height if height % 2 == 1 else height + 1))
        # normalized box kernel
        self.kernel = np.ones((height, width), dtype=float) / (width * height)

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        # extract raw array
        arr = image_data.get_array()
        blurred = Convolver.apply_kernel(arr, self.kernel)
        # update and return
        image_data.image = blurred
        return image_data
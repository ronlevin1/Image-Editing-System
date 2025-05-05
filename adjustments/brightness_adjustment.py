import numpy as np

from core.image_data import ImageData
from operations.filter_decorator import FilterDecorator

"""
BrightnessFilter: scales pixel values to adjust brightness.

Prompts that influenced this implementation:
  • “lets implement the brightness adjustment…”  
  • “explain” (why clip to [0,255])  
  • “why this range is good? ([0.0, 3.0])”  
  • “how do i chain filters? i.e brightness then boxblur”  
"""


class BrightnessFilter(FilterDecorator):
    """
    Adjusts image brightness by scaling pixel values.

    Args:
        factor (float): Multiplicative brightness factor.
            - 1.0 leaves image unchanged
            - <1.0 darkens the image
            - >1.0 brightens the image
        next_filter (Operation, optional): Next filter in chain
    Range:
        factor must be > 0. Recommended range [0.0, 3.0].
    """

    def __init__(self, factor: float, next_filter=None):
        super().__init__(next_filter)
        if factor <= 0:
            raise ValueError("Brightness factor must be > 0")
        self.factor = factor

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        # Work on float copy to prevent overflow
        arr = image_data.get_array().astype(float)
        # Scale brightness
        arr *= self.factor
        # Clip to valid [0,255]
        np.clip(arr, 0, 255, out=arr)
        # Update image and return
        image_data.image = arr.astype(np.uint8)
        return image_data

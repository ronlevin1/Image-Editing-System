from typing import Any

import numpy as np
from operations.base.filter_decorator import FilterDecorator
from core.image_data import ImageData


class ContrastAdjustment(FilterDecorator):
    """
    Concrete decorator for contrast adjustment using the Decorator pattern.
    """

    def __init__(self, value: float, wrapped_operation=None):
        """
        Initialize the contrast adjustment with specified parameters.

        Args:
            value: The factor to adjust contrast by.
                   Range: -10.0 to 10.0 (negative decreases, positive increases contrast)
            wrapped_operation: The next filter in the chain (if any)
        """
        super().__init__(wrapped_operation)

        # Validate value parameter
        if value < -10.0 or value > 10.0:
            raise ValueError("Contrast value must be between -10.0 and 10.0")

        self.value = value

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        """
        Apply contrast adjustment to the image.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data with contrast adjustment applied
        """
        img_float = image_data.image.astype(np.float32)
        mean = np.mean(img_float, axis=(0, 1), keepdims=True)
        adjusted_image = np.clip((img_float - mean) * self.value + mean, 0, 255)
        image_data.image = adjusted_image.astype(image_data.image.dtype)
        return image_data

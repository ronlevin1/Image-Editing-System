from typing import Any

import numpy as np
from operations.base.filter_decorator import FilterDecorator
from core.image_data import ImageData


class ContrastAdjustment(FilterDecorator):
    """
    Concrete decorator for contrast adjustment using the Decorator pattern.
    """

    def __init__(self, factor: float, wrapped_operation=None):
        """
        Initialize the contrast adjustment with specified parameters.

        Args:
            factor: The factor to adjust contrast by.
                   Range: -10.0 to 10.0 (negative decreases, positive increases contrast)
            wrapped_operation: The next filter in the chain (if any)
        """
        super().__init__(wrapped_operation)

        # Validate factor parameter
        if factor < -10.0 or factor > 10.0:
            raise ValueError("Contrast factor must be between -10.0 and 10.0")

        self.factor = factor

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        """
        Apply contrast adjustment to the image.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data with contrast adjustment applied
        """
        # Get the image array
        image = image_data.get_array()

        # Convert factor to a contrast multiplier (1.0 means no change)
        contrast_factor = 1.0 + (self.factor / 10.0)

        # Apply contrast adjustment
        # Formula: (pixel - midpoint) * contrast_factor + midpoint
        midpoint = 127.5  # = 255 / 2
        adjusted = (image.astype(float) - midpoint) * contrast_factor + midpoint

        # Clip to valid range and convert back to uint8
        adjusted = np.clip(adjusted, 0, 255).astype(np.uint8)

        # Update the image data
        image_data.image = adjusted
        return image_data

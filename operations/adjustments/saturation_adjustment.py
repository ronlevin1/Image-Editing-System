import numpy as np
from operations.base.filter_decorator import FilterDecorator
from core.image_data import ImageData


class SaturationAdjustment(FilterDecorator):
    """
    Concrete decorator for saturation adjustment using the Decorator pattern.
    """
    BLUE_WEIGHT = 0.114
    GREEN_WEIGHT = 0.587
    RED_WEIGHT = 0.299

    def __init__(self, factor: float, wrapped_operation=None):
        """
        Initialize the saturation adjustment with specified parameters.

        Args:
            factor: The factor to adjust saturation by.
                   Range: 0.0 to 3.0 (0 = grayscale, 1 = no change, >1 increases saturation)
            wrapped_operation: The next filter in the chain (if any)
        """
        super().__init__(wrapped_operation)

        # Validate factor parameter
        if factor < 0.0:
            raise ValueError("Saturation factor must be non-negative")
        if factor > 3.0:
            raise ValueError("Saturation factor must be at most 3.0")

        self.factor = factor

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        """
        Apply saturation adjustment to the image using pure NumPy.
        """
        # Get the image array
        image = image_data.get_array()

        # Only process if image is not grayscale
        if len(image.shape) == 3 and image.shape[2] >= 3:
            # Convert to float and normalize to [0, 1]
            img_float = image.astype(float) / 255.0

            # Calculate grayscale version (luminance)
            # Standard conversion weights: 0.299 R + 0.587 G + 0.114 B
            grayscale = (self.RED_WEIGHT * img_float[:, :, 0] +
                         self.GREEN_WEIGHT * img_float[:, :, 1] +
                         self.BLUE_WEIGHT * img_float[:, :, 2])
            # align num of dims for next step
            grayscale = np.expand_dims(grayscale, axis=2)

            # Blend between grayscale and color based on saturation factor
            # factor = 0: fully grayscale
            # factor = 1: original image
            # factor > 1: increased saturation
            adjusted = grayscale + self.factor * (img_float - grayscale)

            # Convert back to uint8
            adjusted = np.clip(adjusted * 255.0, 0, 255).astype(np.uint8)

            # Update the image data
            image_data.image = adjusted

        return image_data

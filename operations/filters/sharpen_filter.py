import numpy as np

from core.convolver import Convolver
from core.image_data import ImageData
from operations.base.filter_decorator import FilterDecorator


class SharpenFilter(FilterDecorator):
    # TODO: fix. it doesnt work well, has artifacts.
    """
    Concrete decorator for sharpening filter using the Decorator pattern.

    This filter enhances image edges using the unsharp mask technique:
    1. Blur the image with a Gaussian-like kernel
    2. Subtract the blurred image from the original to get edges
    3. Add the edges back to the original image with a scaling factor
    """
    RADIUS = 2  # constant radius as per requirements

    def __init__(self, amount: float, wrapped_operation=None):
        """
        Initialize the sharpen filter with specified parameters.

        Args:
            amount: The amount of sharpening to apply (scaling factor for edges)
                Recommended range: 0.0 to 5.0.
            wrapped_operation: The operation to be wrapped
        """
        super().__init__(wrapped_operation)

        # Validate amount parameter
        if amount < 0:
            raise ValueError("Sharpening amount must be non-negative")
        if amount > 10.0:
            raise ValueError(
                "Sharpening amount is too large (max recommended: 5.0)")
        elif amount > 5.0:
            print(
                "Warning: High sharpening amounts (>5.0) may cause artifacts")

        # self.amount = amount * 0.1  # can scale down the amount for better control
        self.amount = amount
        # box kernel of size (2*radius+1)=5
        size = self.RADIUS * self.RADIUS + 1
        self.kernel = np.ones((size, size), dtype=float) / (size * size)

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        """
        Apply the sharpen filter to the image.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data with sharpening applied
        """
        # work in float to preserve precision
        original = image_data.get_array().astype(float)
        blurred = Convolver.apply_kernel(original, self.kernel)

        # unsharp mask
        mask = original - blurred

        # add scaled mask back
        sharpened = original + self.amount * mask

        # clip and convert back to uint8
        np.clip(sharpened, 0, 255, out=sharpened)
        image_data.image = sharpened.astype(np.uint8)

        return image_data

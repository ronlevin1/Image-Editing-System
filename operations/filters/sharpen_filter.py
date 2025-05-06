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

    def __init__(self, amount: float, next_filter=None):
        """
        Initialize the sharpen filter with specified parameters.

        Args:
            amount: The amount of sharpening to apply (scaling factor for edges)
                Recommended range: 0.0 to 5.0.
            next_filter: The next filter in the chain (if any)
        """
        super().__init__(next_filter)

        # Validate amount parameter
        if amount < 0:
            raise ValueError("Sharpening amount must be non-negative")
        if amount > 10.0:
            raise ValueError(
                "Sharpening amount is too large (max recommended: 5.0)")
        elif amount > 5.0:
            print(
                "Warning: High sharpening amounts (>5.0) may cause artifacts")

        self.amount = amount * 0.1  # Scale down the amount for better control
        self.radius = self.RADIUS

        # Create a blur kernel for the unsharp mask
        self.blur_kernel = self._create_blur_kernel()

    def _create_blur_kernel(self):
        """
        Create a blur kernel for the unsharp mask.

        Returns:
            A 5x5 kernel approximating a Gaussian blur with radius=2
        """
        # This is a simple approximation of a Gaussian kernel
        kernel = np.array([
            [1, 4, 6, 4, 1],
            [4, 16, 24, 16, 4],
            [6, 24, 36, 24, 6],
            [4, 16, 24, 16, 4],
            [1, 4, 6, 4, 1]
        ], dtype=float)

        # Normalize the kernel so it sums to 1
        return kernel / np.sum(kernel)

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        """
        Apply the sharpen filter to the image.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data with sharpening applied
        """
        # Extract raw array
        original = image_data.get_array()

        # Apply blur to create the mask
        blurred = Convolver.apply_kernel(original, self.blur_kernel)

        # Calculate the unsharp mask (original - blurred)
        mask = original - blurred

        # Apply the mask to the original image with scaling factor
        sharpened = original + self.amount * mask

        # Clip values to valid range [0, 255]
        sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

        # Update image data and return
        image_data.image = sharpened
        return image_data


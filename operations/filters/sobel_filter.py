import numpy as np

from core.convolver import Convolver
from core.image_data import ImageData
from operations.base.filter_decorator import FilterDecorator


class SobelFilter(FilterDecorator):
    """
    Concrete decorator for Sobel edge detection filter using the Decorator pattern.

    This filter applies two Sobel convolution kernels to detect edges in
    horizontal and vertical directions, then combines them to highlight edges.
    """

    def __init__(self, next_filter=None):
        super().__init__(next_filter)
        # Sobel kernel for horizontal edges (x-direction)
        self.kernel_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ], dtype=float)

        # Sobel kernel for vertical edges (y-direction)
        self.kernel_y = np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ], dtype=float)

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        # Extract raw array
        arr = image_data.get_array()

        # Convert to grayscale if it's a color image
        if len(arr.shape) == 3 and arr.shape[2] == 3:
            # Simple grayscale conversion - average of RGB channels
            arr_gray = np.mean(arr, axis=2)
        else:
            arr_gray = arr

        # Apply horizontal and vertical Sobel kernels
        gradient_x = Convolver.apply_kernel(arr_gray, self.kernel_x)
        gradient_y = Convolver.apply_kernel(arr_gray, self.kernel_y)

        # Compute gradient magnitude
        gradient_magnitude = np.sqrt(
            np.square(gradient_x) + np.square(gradient_y))

        # Normalize to enhance visibility - scale to use full 0-255 range
        if np.max(gradient_magnitude) > 0:  # Avoid division by zero
            gradient_magnitude = gradient_magnitude * (
                    255.0 / np.max(gradient_magnitude))

        # Convert to proper data type for display
        gradient_magnitude = gradient_magnitude.astype(np.uint8)

        # If original was color, convert result back to RGB format
        if len(arr.shape) == 3 and arr.shape[2] == 3:
            gradient_magnitude = np.stack([gradient_magnitude] * 3, axis=2)

        # Update and return
        image_data.image = gradient_magnitude
        return image_data

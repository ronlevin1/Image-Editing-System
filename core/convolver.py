import numpy as np

"""
Convolver: low-level convolution routines for applying kernels to images.

Prompts that influenced this implementation:
  • “implement this code file”  
  • “explain this please” (kernel flipping rationale)  
  • “demonstrate what are the values of each line” (padding, output shape)  
  • “in the last iteration [#9], does the region cover the area such that the center-pixel is the pixel of row 9 in the original image?”  
  • “why should [kernel dimensions] be odd?”  
  • “what should be the effect of kernel of ones?”  
"""


class Convolver:
    """
    Provides low-level convolution routines for applying kernels to images.
    """

    @staticmethod
    def apply_kernel(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Convolves the given image with the specified kernel.

        Args:
            image: numpy array of shape (H, W) or (H, W, C)
            kernel: 2D numpy array of shape (kernel_h, kernel_w)

        Returns:
            Convolved image array of the same shape as input.
        """
        # Ensure kernel dimensions are odd
        kernel_h, kernel_w = kernel.shape
        pad_h = kernel_h // 2
        pad_w = kernel_w // 2

        # Pad image with edge padding
        if image.ndim == 2:  # 2D = grayscale img
            padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)),
                            mode='edge')
            return Convolver._convolve_2d(padded, kernel)

        elif image.ndim == 3:  # 3D = colored img
            channels = []
            for c in range(image.shape[2]):
                channel = image[:, :, c]
                padded = np.pad(channel, ((pad_h, pad_h), (pad_w, pad_w)),
                                mode='edge')
                convolved = Convolver._convolve_2d(padded, kernel)
                channels.append(convolved)
            return np.stack(channels, axis=2)
        else:
            raise ValueError("Image must be 2D or 3D array")

    @staticmethod
    def _convolve_2d(padded_img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Helper for 2D convolution on a padded image.

        Args:
            padded_img: padded 2D array
            kernel: 2D kernel array

        Returns:
            2D convolved array cropped to original size
        """
        H, W = padded_img.shape
        kernel_h, kernel_w = kernel.shape
        output_h = H - kernel_h + 1
        output_w = W - kernel_w + 1
        result = np.zeros((output_h, output_w), dtype=padded_img.dtype)

        # (optional) Flip kernel for convolution
        flipped_kernel = np.flipud(np.fliplr(kernel))

        for i in range(output_h):
            for j in range(output_w):
                # the current region in padded image, covered by the kernel
                region = padded_img[i:i + kernel_h, j:j + kernel_w]
                result[i, j] = np.sum(region * flipped_kernel)

        return result

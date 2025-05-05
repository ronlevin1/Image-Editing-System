import numpy as np

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
            kernel: 2D numpy array of shape (kH, kW)

        Returns:
            Convolved image array of the same shape as input.
        """
        # Ensure kernel dimensions are odd
        kH, kW = kernel.shape
        pad_h = kH // 2
        pad_w = kW // 2

        # Pad image with edge padding
        if image.ndim == 2: # 2D = grayscale img
            padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
            return Convolver._convolve_2d(padded, kernel)

        elif image.ndim == 3: # 3D = colored img
            channels = []
            for c in range(image.shape[2]):
                channel = image[:, :, c]
                padded = np.pad(channel, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
                convolved = Convolver._convolve_2d(padded, kernel)
                channels.append(convolved)
            return np.stack(channels, axis=2)
        else:
            raise ValueError("Image must be 2D or 3D array")

    @staticmethod
    def _convolve_2d(padded: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Helper for 2D convolution on a padded image.

        Args:
            padded: padded 2D array
            kernel: 2D kernel array

        Returns:
            2D convolved array cropped to original size
        """
        H, W = padded.shape
        kH, kW = kernel.shape
        out_h = H - kH + 1
        out_w = W - kW + 1
        result = np.zeros((out_h, out_w), dtype=padded.dtype)

        # (optional) Flip kernel for convolution
        flipped = np.flipud(np.fliplr(kernel))

        for i in range(out_h):
            for j in range(out_w):
                region = padded[i:i + kH, j:j + kW]
                result[i, j] = np.sum(region * flipped)

        return result


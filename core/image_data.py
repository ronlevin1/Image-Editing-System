from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


class ImageData:
    """
    Core class for handling image I/O and display.
    Provides load, save, and show functionality.
    """

    def __init__(self, image_data):
        """
        Initialize with either a PIL Image or numpy array.

        Args:
            image_data: Either a PIL Image or numpy array
        """
        if isinstance(image_data, np.ndarray):
            self.image = image_data
        elif isinstance(image_data, Image.Image):
            self.image = np.array(image_data)
        else:
            raise TypeError(f"Expected PIL Image or numpy ndarray, got {type(image_data)}")

    @staticmethod
    def load(path: str) -> 'ImageData':
        """
        Load an image from a file and return an ImageData instance.
        """
        img = Image.open(path).convert('RGB')
        return ImageData(img)

    def save(self, path: str):
        """
        Save the image to the specified path.
        """
        img = Image.fromarray(self.image.astype(np.uint8))
        img.save(path)

    def show(self):
        """
        Display the image using matplotlib.
        """
        plt.imshow(self.image)
        plt.axis('off')
        plt.show()

    def get_array(self) -> np.ndarray:
        """
        Return the internal NumPy array.
        """
        return self.image
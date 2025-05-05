from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""
ImageData: loading, saving, and displaying images.

Prompts that influenced this implementation:
  • “implement ImageData class to provide the functionality needed for this project”  
"""


class ImageData:
    """
    Core class for handling image I/O and display.
    Provides load, save, and show functionality.
    """

    def __init__(self, image_array: np.ndarray):
        self.image = image_array

    @staticmethod
    def load(path: str) -> 'ImageData':
        """
        Load an image from a file and return an ImageData instance.
        """
        img = Image.open(path).convert('RGB')
        return ImageData(np.array(img))

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

# TODO: maybe add more functionality

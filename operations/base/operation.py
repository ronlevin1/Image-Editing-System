"""Abstract base class for all image operations."""
from abc import ABC, abstractmethod
from typing import Any


class Operation(ABC):
    """Base interface for all image editing operations."""

    def __init__(self):
        """
        Constructor for the Operation class.
        In Java-like style, we include an explicit constructor.
        """
        super().__init__()

    @abstractmethod
    def apply(self, image_data: Any) -> Any:
        """
        Abstract method that must be implemented by concrete subclasses.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data
        """
        pass
"""Base decorator class implementing decorator pattern."""
from abc import abstractmethod
from typing import Any

from .operation import Operation


class FilterDecorator(Operation):
    """
    Base decorator class that wraps another operation.
    Similar to Java's Decorator pattern implementation.
    """

    def __init__(self, next_filter: Operation = None):
        """
        Constructor for the FilterDecorator class.

        Args:
            next_filter: The operation to be called after this one
        """
        super().__init__()
        self._next_filter = next_filter

    def apply(self, image_data: Any) -> Any:
        """
        Template method pattern: calls internal _apply_filter,
        then delegates to wrapped operation.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data
        """
        processed_img = self._apply_filter(image_data)

        if self._next_filter is None:
            return processed_img
        else:
            return self._next_filter.apply(processed_img)

    @abstractmethod
    def _apply_filter(self, image_data: Any) -> Any:
        """
        Abstract method to be implemented by concrete filters.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data
        """
        pass
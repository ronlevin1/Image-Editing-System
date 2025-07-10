"""Base decorator class implementing decorator pattern."""
from abc import abstractmethod
from typing import Any

from .operation import Operation
from core.image_data import ImageData


class FilterDecorator(Operation):
    """
    Base decorator class that wraps another operation.
    Similar to Java's Decorator pattern implementation.
    """

    def __init__(self, wrapped_filter: Operation = None):
        """
        Constructor for the FilterDecorator class.

        Args:
            wrapped_filter: The operation to be wrapped
        """
        super().__init__()
        self._wrapped_filter = wrapped_filter

    def set_wrapped_filter(self, wrapped_filter: Operation) -> None:
        """
        Sets the wrapped operation.

        Args:
            wrapped_filter: The operation to be wrapped
        """
        self._wrapped_filter = wrapped_filter

    def apply(self, image_data: Any) -> Any:
        """
        Template method pattern: delegates to wrapped operation,
        then calls internal _apply_filter.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data
        """
        processed_img = image_data
        if self._wrapped_filter:
            processed_img = self._wrapped_filter.apply(image_data)

        return self._apply_filter(processed_img)

    @abstractmethod
    def _apply_filter(self, image_data: ImageData) -> Any:
        """
        Abstract method to be implemented by concrete filters.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data
        """
        pass
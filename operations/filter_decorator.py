"""Base decorator class implementing decorator pattern."""
from abc import abstractmethod
from typing import Any

from .operation import Operation


class FilterDecorator(Operation):
    """
    Base decorator class that wraps another operation.
    Similar to Java's Decorator pattern implementation.
    """

    def __init__(self, wrapped_operation: Operation = None):
        """
        Constructor for the FilterDecorator class.

        Args:
            wrapped_operation: The operation to be called after this one
        """
        super().__init__()
        self._wrapped = wrapped_operation

    def apply(self, image_data: Any) -> Any:
        """
        Template method pattern: calls internal _apply_filter,
        then delegates to wrapped operation.

        Args:
            image_data: The image data to process

        Returns:
            The processed image data
        """
        processed_data = self._apply_filter(image_data)

        if self._wrapped is None:
            return processed_data
        else:
            return self._wrapped.apply(processed_data)

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
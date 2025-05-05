"""
Factory for creating operation objects from configuration.
Implements the Simple Factory design pattern.
"""
from typing import Dict, Any

from .operation import Operation

# TODO
# from ..filters.box_blur import BoxBlurFilter
# from ..filters.sobel import SobelFilter
# from ..filters.sharpen import SharpenFilter
# from ..adjustments.brightness import BrightnessAdjustment
# from ..adjustments.contrast import ContrastAdjustment
# from ..adjustments.saturation import SaturationAdjustment


class OperationFactory:
    """
    Factory for creating operation objects based on configuration.
    Uses direct if-else logic similar to Java factory implementations.
    """

    def __init__(self):
        """
        Constructor for the OperationFactory class.
        """
        super().__init__()

    @staticmethod
    def create(operation_config: Dict[str, Any]) -> Operation:
        """
        Create an operation instance from a configuration dictionary.

        Args:
            operation_config: Dict with 'type' and parameters

        Returns:
            An initialized Operation object

        Raises:
            ValueError: If operation type is unknown or parameters are invalid
        """
        if 'type' not in operation_config:
            raise ValueError("Operation config must include 'type' field")

        operation_type = operation_config['type']

        # Extract parameters (excluding the 'type' field)
        parameters = {k: v for k, v in operation_config.items() if k != 'type'}

        # Determine which operation to create based on type
        if operation_type == "box":
            return BoxBlurFilter(**parameters)
        elif operation_type == "sobel":
            return SobelFilter(**parameters)
        elif operation_type == "sharpen":
            return SharpenFilter(**parameters)
        elif operation_type == "brightness":
            return BrightnessAdjustment(**parameters)
        elif operation_type == "contrast":
            return ContrastAdjustment(**parameters)
        elif operation_type == "saturation":
            return SaturationAdjustment(**parameters)
        else:
            raise ValueError(f"Unknown operation type: {operation_type}")
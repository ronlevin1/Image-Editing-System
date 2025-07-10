"""
Factory for creating operation objects from configuration.
Implements the Simple Factory design pattern.
"""
from typing import Dict, Any
from operations.base.operation import Operation
from operations.filters.box_blur_filter import BoxBlurFilter
from operations.filters.sobel_filter import SobelFilter
from operations.filters.sharpen_filter import SharpenFilter
from operations.adjustments.brightness_adjustment import \
    BrightnessAdjustment
from operations.adjustments.contrast_adjustment import \
    ContrastAdjustment
from operations.adjustments.saturation_adjustment import \
    SaturationAdjustment


class OperationFactory:
    """
    Factory for creating operation objects based on configuration.
    Uses direct if-else logic similar to Java factory implementations.
    """
    _operation_map = {
        "box": BoxBlurFilter,
        "sobel": SobelFilter,
        "sharpen": SharpenFilter,
        "brightness": BrightnessAdjustment,
        "contrast": ContrastAdjustment,
        "saturation": SaturationAdjustment
    }

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
        # extract operation type and parameters
        operation_type = operation_config['type'].lower()

        parameters = {}
        for k, v in operation_config.items():
            if k != 'type':
                parameters[k] = v

        # Determine which operation to create based on type
        operation_class = OperationFactory._operation_map.get(operation_type)
        if operation_class:
            return operation_class(**parameters)

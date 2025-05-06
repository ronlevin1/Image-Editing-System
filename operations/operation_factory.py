"""
Factory for creating operation objects from configuration.
Implements the Simple Factory design pattern.
"""
from typing import Dict, Any
from operations.base.operation import Operation


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
        # TODO: fix all imports all over project
        from operations.filters.box_blur_filter import BoxBlurFilter
        from operations.filters.sobel_filter import SobelFilter
        # from filters.sharpen import SharpenFilter

        from operations.adjustments.brightness_adjustment import \
            BrightnessAdjustment
        # from adjustments.contrast import ContrastAdjustment
        # from adjustments.saturation import SaturationAdjustment

        if 'type' not in operation_config:
            raise ValueError("Operation config must include 'type' field")

        # extract operation type and parameters
        operation_type = operation_config['type'].lower()

        parameters = {}
        for k, v in operation_config.items():
            if k != 'type':
                parameters[k] = v

        OperationFactory._validate_parameters(parameters, operation_type)

        # TODO: uncomment post implementing
        # Determine which operation to create based on type
        if operation_type in ["box", "boxblur"]:
            return BoxBlurFilter(**parameters)
        elif operation_type == "sobel":
            return SobelFilter(**parameters)
        # elif operation_type == "sharpen":
        #     return SharpenFilter(**parameters)
        elif operation_type == "brightness":
            return BrightnessAdjustment(**parameters)
        # elif operation_type == "contrast":
        #     return ContrastAdjustment(**parameters)
        # elif operation_type == "saturation":
        #     return SaturationAdjustment(**parameters)
        else:
            raise ValueError(f"Unknown operation type: {operation_type}")

    @staticmethod
    def _validate_parameters(extracted_parameters: Dict[str, Any],
                             operation_type: str) -> None:
        """
        Validate the parameters for the operation.

        Args:
            extracted_parameters: Dictionary of parameters to validate

        Raises:
            ValueError: If any parameter is invalid
        """
        # Define required parameters for each operation type
        required_params = {
            "box": ["width", "height"],
            "boxblur": ["width", "height"],
            "brightness": ["factor"],
            "sobel": []
        }
            # TODO: Add more as you implement them

        # Define parameter types for validation
        param_types = {
            "box": {"width": int, "height": int},
            "boxblur": {"width": int, "height": int},
            "brightness": {"factor": float},
            "sobel": {}
            # TODO: Add more as you implement them
        }

        # Validate parameters
        if operation_type in required_params:
            # Check if all required parameters are present
            for param in required_params[operation_type]:
                if param not in extracted_parameters:
                    raise ValueError(
                        f"Missing required parameter '{param}' for {operation_type}")

        # Check parameter types
        if operation_type in param_types:
            for param, expected_type in param_types[operation_type].items():
                if param in extracted_parameters and not isinstance(
                        extracted_parameters[param], expected_type):
                    raise ValueError(
                        f"Parameter '{param}' for {operation_type} "
                        f"must be a {expected_type.__name__}")

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
        from operations.filters.box_blur_filter import BoxBlurFilter
        from operations.filters.sobel_filter import SobelFilter
        from operations.filters.sharpen_filter import SharpenFilter

        from operations.adjustments.brightness_adjustment import \
            BrightnessAdjustment
        from operations.adjustments.contrast_adjustment import \
            ContrastAdjustment
        from operations.adjustments.saturation_adjustment import \
            SaturationAdjustment

        if 'type' not in operation_config:
            raise ValueError("Operation config must include 'type' field")

        # extract operation type and parameters
        operation_type = operation_config['type'].lower()

        parameters = {}
        for k, v in operation_config.items():
            if k != 'type':
                parameters[k] = v

        OperationFactory._normalize_parameter_names(operation_type, parameters)

        OperationFactory._validate_parameters(parameters, operation_type)

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

    @staticmethod
    def _normalize_parameter_names(operation_type, parameters):
        """
        Map "value" to the appropriate parameter name based on operation type and ensure correct type conversion.
        """
        param_mappings = {
            "brightness": "factor",
            "contrast": "factor",
            "saturation": "factor",
            "sharpen": "amount"
        }

        # Define expected types for each parameter
        param_types = {
            "brightness": {"factor": float},
            "contrast": {"factor": float},
            "saturation": {"factor": float},
            "sharpen": {"amount": float}
        }

        if operation_type in param_mappings and "value" in parameters:
            canonical_param_name = param_mappings[operation_type]
            # Only map if original parameter isn't present
            if canonical_param_name not in parameters:
                # Convert to expected type if needed
                if (operation_type in param_types and
                        canonical_param_name in param_types[operation_type]):
                    expected_type = param_types[operation_type][canonical_param_name]
                    parameters[canonical_param_name] = expected_type(parameters["value"])
                else:
                    parameters[canonical_param_name] = parameters["value"]

                # Remove "value" to avoid passing extra parameters
                del parameters["value"]

    @staticmethod
    def _validate_parameters(extracted_parameters: Dict[str, Any],
                             operation_type: str) -> None:
        """
        Validate the parameters for the operation.

        Args:
            extracted_parameters: Dictionary of parameters to validate
            operation_type: Type of the operation

        Raises:
            ValueError: If any parameter is invalid
        """
        # Define required parameters for each operation type
        # For single-parameter operations, we'll allow either "factor"/"amount" OR "value"
        required_params = {
            "box": ["width", "height"],
            "brightness": [["factor", "value"]],
            # Either factor or value is required
            "sobel": [],
            "sharpen": [["amount", "value"]],
            # Either amount or value is required
            "contrast": [["factor", "value"]],
            # Either factor or value is required
            "saturation": [["factor", "value"]],
            # Either factor or value is required
        }

        # Define parameter types for validation
        param_types = {
            "box": {"width": int, "height": int},
            "brightness": {"factor": float, "value": float},
            "sobel": {},
            "sharpen": {"amount": float, "value": float},
            "contrast": {"factor": float, "value": float},
            "saturation": {"factor": float, "value": float},
        }

        # Validate parameters
        if operation_type in required_params:
            # Check if all required parameters are present
            for param in required_params[operation_type]:
                # Handle alternative parameters (lists)
                if isinstance(param, list):
                    # Check if at least one of the alternatives is present
                    if not any(alt in extracted_parameters for alt in param):
                        raise ValueError(
                            f"Missing required parameter (one of {' or '.join(param)}) for {operation_type}")
                elif param not in extracted_parameters:
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

    # @staticmethod
    # def _validate_parameters(extracted_parameters: Dict[str, Any],
    #                          operation_type: str) -> None:
    #     """
    #     Validate the parameters for the operation.
    #
    #     Args:
    #         extracted_parameters: Dictionary of parameters to validate
    #
    #     Raises:
    #         ValueError: If any parameter is invalid
    #     """
    #     # Define required parameters for each operation type
    #     required_params = {
    #         "box": ["width", "height"],
    #         "brightness": ["factor"],
    #         "sobel": [],
    #         "sharpen": ["amount"],
    #         "contrast": ["factor"],
    #         "saturation": ["factor"],
    #     }
    #
    #     # Define parameter types for validation
    #     param_types = {
    #         "box": {"width": int, "height": int},
    #         "brightness": {"factor": float},
    #         "sobel": {},
    #         "sharpen": {"amount": float},
    #         "contrast": {"factor": float},
    #         "saturation": {"factor": float},
    #     }
    #
    #     # Validate parameters
    #     if operation_type in required_params:
    #         # Check if all required parameters are present
    #         for param in required_params[operation_type]:
    #             if param not in extracted_parameters:
    #                 raise ValueError(
    #                     f"Missing required parameter '{param}' for {operation_type}")
    #
    #     # Check parameter types
    #     if operation_type in param_types:
    #         for param, expected_type in param_types[operation_type].items():
    #             if param in extracted_parameters and not isinstance(
    #                     extracted_parameters[param], expected_type):
    #                 raise ValueError(
    #                     f"Parameter '{param}' for {operation_type} "
    #                     f"must be a {expected_type.__name__}")

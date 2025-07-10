import json
import os
from typing import Dict, Any


class Config:
    """
    Configuration class that holds all parsed data from a JSON configuration file.
    """

    def __init__(self, config_file_path: str):
        self.config_dict = self._load_from_file(config_file_path)

        # store configuration values as instance properties
        self.input_path = self.config_dict['input']
        self.output_path = self.config_dict.get('output', None)
        self.display = self.config_dict.get('display', False)
        self.operations_config = self.config_dict.get('operations', [])

        self._validate()

    def _load_from_file(self, file_path: str) -> dict:
        """
        Load configuration from a JSON file.

        Template of the output dictionary:
        {
            'input': 'string (required, path to input image)',
            'output': 'string (optional, path to save output image)',
            'display': True,  # or False, depending on the actual boolean value
            'operations': [
                {
                    'type': 'string (required)',
                    '<parameter_key>': '<parameter_value>'
                }
            ]
        }
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    def _validate(self) -> None:
        """Validate the configuration according to requirements."""
        # Check for required input field
        if 'input' not in self.config_dict or not self.config_dict['input']:
            raise ValueError("Configuration must contain a valid 'input' path")

        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")

        # Check that at least output or display:true is specified
        if not (self.output_path or self.display):
            raise ValueError(
                "Configuration must specify either an output path or display=true (or both)")

        for op in self.operations_config:
            if 'type' not in op:
                raise ValueError("Operation config must include 'type' field")
            self._validate_parameters(op)

    def _validate_parameters(self, operation_config: Dict[str, Any]) -> None:
        """
        Validate the parameters for the operation.
        """
        operation_type = operation_config['type'].lower()
        parameters = {k: v for k, v in operation_config.items() if k != 'type'}

        required_params = {
            "box": ["width", "height"],
            "brightness": ["value"],
            "sobel": [],
            "sharpen": ["value"],
            "contrast": ["value"],
            "saturation": ["value"],
        }

        param_types = {
            "box": {"width": int, "height": int},
            "brightness": {"value": float},
            "sobel": {},
            "sharpen": {"value": float},
            "contrast": {"value": float},
            "saturation": {"value": float},
        }

        if operation_type in required_params:
            for param in required_params[operation_type]:
                if param not in parameters:
                    raise ValueError(
                        f"Missing required parameter '{param}' for {operation_type}")

        if operation_type in param_types:
            for param, expected_type in param_types[operation_type].items():
                if param in parameters and not isinstance(parameters[param], expected_type):
                    raise ValueError(
                        f"Parameter '{param}' for {operation_type} "
                        f"must be a {expected_type.__name__}")

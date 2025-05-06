import json


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

        # Check that at least output or display:true is specified
        if not (self.output_path or self.display):
            raise ValueError(
                "Configuration must specify either an output path or display=true (or both)")

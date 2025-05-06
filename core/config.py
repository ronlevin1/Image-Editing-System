import json
from operations.operation_factory import OperationFactory


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

        # TODO: delete after testing
        # Create operation pipeline
        # self.operation_pipeline = self._create_operation_pipeline()

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

# TODO: delete after testing
    # def _create_operation_pipeline(self):
    #     """Create a pipeline of operations from configuration."""
    #     if 'operations' not in self.config_dict:
    #         raise ValueError("Configuration must contain 'operations' list")
    #
    #     operations = self.config_dict['operations'] # list of dicts
    #     if not operations:
    #         raise ValueError("At least one operation must be specified")
    #
    #     # Create operation objects
    #     operations_chain = []
    #     for op_config in operations:
    #         current_config = op_config.copy()
    #         current_config.pop('next_filter', None)  # a defensive step,
    #                                           # although this shouldn't happen
    #         current_operation = OperationFactory.create(current_config)
    #         operations_chain.append(current_operation)
    #
    #     # Chain operations
    #     for i in range(len(operations_chain) - 1):
    #         operations_chain[i].set_next_filter(operations_chain[i + 1])
    #
    #     return operations_chain[0] if operations_chain else None

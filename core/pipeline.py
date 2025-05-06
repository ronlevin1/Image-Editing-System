# core/pipeline.py
from operations.operation_factory import OperationFactory
from typing import List, Dict, Any

class OperationPipeline:
    """Manages creation and execution of operation pipelines."""

    @staticmethod
    def create_from_config(operations_config: List[Dict[str, Any]]):
        """Create a pipeline of operations from configuration."""
        if not operations_config:
            raise ValueError("At least one operation must be specified")

        # Create operation objects
        operations_chain = []
        for op_config in operations_config:
            current_config = op_config.copy()
            current_config.pop('next_filter', None) # a defensive step,
                                        # although this shouldn't happen
            current_operation = OperationFactory.create(current_config)
            operations_chain.append(current_operation)

        # Chain operations
        for i in range(len(operations_chain) - 1):
            operations_chain[i].set_next_filter(operations_chain[i + 1])

        return operations_chain[0] if operations_chain else None
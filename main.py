#!/usr/bin/env python3
import argparse
import json
import sys
from core.config import Config
from core.pipeline import OperationPipeline
from core.image_data import ImageData

"""
This is the main file.
"""


def printUI(i):
    if i == 0:
        print("\n" + "=" * 60)
        print("\tRUNNING, this might take a minute.")
        print("" + "=" * 60)
        print(
            "\n>> NOTE: if running a test on a series of images with config 'display':true,\n"
            "\t make sure to close the output images window after each one.\n"
            "\t Otherwise - the execution will halt.\n")
    elif i == 1:
        print("\n" + "=" * 60)
        print("\n>> Done.\n")


def main():
    """
        Main function for the image processing CLI.

        Process:
        1. Parse command line arguments to get the config file path.
        2. Create a Config object that handles loading and validation.
        3. Create the operation pipeline using OperationPipeline.create_from_config().
        4. Load the image, apply the pipeline, and handle output/display.

        Returns:
            None

        Raises:
            FileNotFoundError: If the config file or input image cannot be found.
            json.JSONDecodeError: If the config file contains invalid JSON.
            ValueError: If the configuration is invalid.
        """
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    args = parser.parse_args()

    try:
        # Create config object which loads, validates and prepares operations
        config = Config(args.config)
        pipeline = OperationPipeline.create_from_config(
            config.operations_config)
        image = ImageData.load(config.input_path)
        result = pipeline.apply(image)

        # Print each operation configuration
        print(">> Applied the following operations:")
        for i, operation in enumerate(config.operations_config):
            print(f"\t{i + 1}. {operation}")

        # Handle output based on configuration
        if config.output_path:
            result.save(config.output_path)
            print(f"Image saved to {config.output_path}")

        # Handle display option
        if config.display:
            result.show()

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    printUI(0)
    main()
    printUI(1)

import argparse
import json
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from core.config import Config
from core.pipeline import OperationPipeline
from core.image_data import ImageData



def main():
    parser = argparse.ArgumentParser(description='Image Editing Tool')
    parser.add_argument('--config', required=True,
                        help='Path to configuration JSON file')
    args = parser.parse_args()

    try:
        # Create config object which loads, validates and prepares operations
        config = Config(args.config)
        operation_pipeline = OperationPipeline.create_from_config(config.operations_config)

        # Load the input image
        image = ImageData.load(config.input_path)

        # Apply the operation pipeline
        processed_image = operation_pipeline.apply(image)

        # Print each operation configuration
        print("Applied the following operations:")
        for i, operation in enumerate(config.operations_config):
            print(f"{i + 1}. {operation}")

        # Handle output based on configuration
        if config.output_path:
            Image.fromarray(processed_image).save(config.output_path)
            print(f"Image saved to {config.output_path}")

        # Handle display option
        if config.display:
            plt.figure()  # figsize=(10, 10)
            plt.imshow(processed_image)
            plt.axis('off')
            plt.title("Processed Image")
            plt.show()

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

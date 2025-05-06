import argparse
import json
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from core.config import ConfigLoader

def main():
    # Parse command line arguments to get config_path
    parser = argparse.ArgumentParser(description='Image Editing Tool')
    parser.add_argument('--config', required=True, help='Path to configuration JSON file')
    args = parser.parse_args()

    try:
        # Load configuration
        config = ConfigLoader.load_from_file(args.config)

        # Validate configuration
        ConfigLoader.validate_config(config)

        # Create operation pipeline
        operation_pipeline = ConfigLoader.create_operation_pipeline(config)

        # Load the input image
        input_path = config['input']
        image = np.array(Image.open(input_path))

        # Apply the operation pipeline
        processed_image = operation_pipeline.apply(image)

        # Handle output based on configuration
        if 'output' in config and config['output']:
            output_path = config['output']
            Image.fromarray(processed_image).save(output_path)
            print(f"Image saved to {output_path}")

        # Handle display option
        if 'display' in config and config['display'] is True:
            plt.figure(figsize=(10, 10))
            plt.imshow(processed_image)
            plt.axis('off')
            plt.title("Processed Image")
            plt.show()

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
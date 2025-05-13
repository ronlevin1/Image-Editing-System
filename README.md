# Image Editing System
###### author:  Ron Levin, May 2025.

A command-line image processing tool that allows applying various filters and 
adjustments to images through configuration files.

## Features
- Apply multiple image operations in sequence
- Supported operations:
  - Filters: Box blur, Sobel, Sharpen
  - Adjustments: Brightness, Contrast, Saturation
- Save/display processed images or interactively

## Requirements
- Python 3.8+
- Required packages: NumPy, Pillow, matplotlib

## Usage
- Run the tool from the command line with the following structure:
  - ./main.py --config path_to_config.json
- Or alternatively:
  - python3 main.py --config path_to_config.json 

## Configuration
- Template example for configuration file:
  - See filter files for specific parameter names.
```json
{
  'input': 'string (required, path to input image)',
  'output': 'string (optional, path to save output image)',
  'display': "<True>, or <False>, depending on the actual boolean value"
  'operations': [
    {
      'type': 'string (required)',
      '<parameter_key>': '<parameter_value>'
    }
  ]
}
```

## Known Issues
- The sharpen filter may produce artifacts in some cases.

## TODOs:
1. fix base decorator order of apply() calls
2. factory:
   - change to hashmap 
   - clean up validation
3. config:
   - pull input and operations validation to the config class
4. filter classes:
    - remove extraction to np.array(), this is redundant

## Project Structure
- See the info/project_structure.txt file for details on the codebase organization.


## LLMs
- I used the following LLMs to assist me in the project:
  - GitHub Copilot (mainly with Claude 3.7 sonnet Thinking)
  - ChatGPT (o4-mini Reasoning model)
  - Perplexity AI

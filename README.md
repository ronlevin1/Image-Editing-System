# Lightricks Image Processor
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
  - ./edit-image.py --config path_to_config.json
- Or alternatively:
  - python3 edit-image.py --config path_to_config.json 

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

## Project Structure
- See the info/project_structure.txt file for details on the codebase organization.


-------------------------------------------------------------------------------

## LLMs
- I used the following LLMs to assist me in the project:
  - GitHub Copilot (mainly with Claude 3.7 sonnet Thinking)
  - ChatGPT (o4-mini Reasoning model)
  - Perplexity AI
  
### Prompts used
- These are prompts I used additionally to those specified in the code
- Topic - discussing generally about the project

1. 
   * (attached instructions file)
   * Prompt: "read the file. suggest a program structure for the description
     in it. dont give code, structure and design only. in your answer, explain
     the design you chose and the category of each component. i.e, i was
     thinking that each filter should be an instance of some
     decorator. in that way, when user want to apply a few filters
     consecutively, it can be possible easily. in addition, it allows easy
     extension. this was an example so far, but if it is a good idea, consider
     it yourself. again - focus now on structure and design of program and its
     components only.
2. 
    * Prompt: "What are the pros and cons of using the Decorator pattern versus
      the Strategy pattern in this context?"
    * Response Summary: #TODO
      Use the Decorator Pattern if dynamic composition and runtime flexibility
      are priorities.
      Use the Strategy Pattern if simplicity, decoupling, and ease of debugging
      are more important.
3. 
    * Prompt: "suggest the project structure in the means of seperation to
      packages, files, etc. no code for now."
    * "this project seems large and complex. can you simplify it by reducing
      number of files, or something else? i dont have much time to work on it"
4. 
    * Prompt: "lets implemt the decorator design pattern. provide code too in
      this step. one file by another"
    * "i want to let you know that im not familiar with OOP syntax in python. i
      learned OOP in java. is it possible to modify the code structure to match
      that one of java? in the means of logic, structure, etc"
    * "im not familiar with registry pattern. modify it to be simple factory"
5. 
    * (After beginning with implementing the Decorator pattern)
    * Prompt: "i dont fully understand what were doing. do you think we should
      implement the rest of the project top-down or bottom-up?"
    * Response Summary: Recommended bottom-up approach with implementation
      order starting with ImageData class, then filters, adjustments, factory,
      pipeline, and CLI.

6. * To test the different filter, i asked Perplexity to find a good image 
   * suitable for each filter.

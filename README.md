# Lightricks_HA

An image processing program, given as home assignment by Lightricks.
* To run this program, you need to have Python 3.8 or higher installed.
* You should be able to run the tool from the command line using the following 
structure "./edit-image --config path_to_config.json".
* (Remember to be in the directory where the program is located)
* NOTICE: you have to use './' in the command: "./edit-image ...". 
* Alternativly, run it with "python3 edit-image.py ...".

Additional prompts I used, discussing generally about the project:

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
3.
    * (After beginning with implementing the Decorator pattern)
    * Prompt: "i dont fully understand what were doing. do you think we should
      implement the rest of the project top-down or bottom-up?"
    * Response Summary: Recommended bottom-up approach with implementation
      order starting with ImageData class, then filters, adjustments, factory,
      pipeline, and CLI.

#TODO next:

3. Complete other filters and adjustments
   Implement the rest of the filters (e.g. sharpen, contrast, etc.) and
   adjustments (e.g. brightness, gamma).

   Ensure they are chainable and work with the pipeline builder.

   Unit-test each filter and adjustment separately.

4. Finish Factory

   Implement the factory method to create the correct filter object based on
   the descriptor.

   Ensure it handles all filters and adjustments correctly.

   Unit-test the factory method with various descriptors.

5. Final Tests & Polish

   End-to-end test with a sample JSON: load → apply 3 filters → save/display.

   Add error handling (invalid kernel sizes, missing ﬁles).

   Clean up: remove debug code, add docstrings, and prepare README.


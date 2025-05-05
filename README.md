# Lightricks_HA

image proccesing program, given as home assignment.

#TODO next:

1. Pipeline Builder

   Write a helper that takes a list of filter descriptors (e.g. ("box",5,5), ("
   brightness",0.6)) and instantiates a single chained object.

   Unit-test mapping from descriptor list → correct filter chain.

2. CLI / Config Integration

   Parse JSON config into a list of operation descriptors.

   Use your pipeline builder to create the chain.

   Load the image, run the chain, then save or show based on config flags.

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


import unittest

import numpy as np
from core.image_data import ImageData
from operations.filter_decorator import FilterDecorator
from filters.box_blur_filter import BoxBlurFilter
from operations.operation import Operation

"""
NoOpFilter: passes image through unchanged.

Prompts that influenced this implementation:
  • “implement this one please”  
  • “generate a test code for NoOpfilter”  
"""


class NoOpFilter(Operation):
    def apply(self, image_data: ImageData) -> ImageData:
        return image_data


class DummyFilter(FilterDecorator):
    """A dummy filter that multiplies all pixels by 2."""

    def _apply_filter(self, image_data: ImageData) -> ImageData:
        arr = image_data.get_array()
        image_data.image = arr * 2
        return image_data


# class TestBoxBlurFilter(unittest.TestCase):
#     def test_box_blur_uniform(self):
#         # 3×3 image with values 1…9
#         arr = np.ones((3,3), dtype=float) * 5
#         img = ImageData(arr.copy())
#         # 3×3 box blur will average all 9 values = (5*9)/9 = 5
#         blur = BoxBlurFilter(width=3, height=3)
#         out = blur.apply(img).get_array()
#         expected = np.full((3, 3), 5.0)
#         np.testing.assert_allclose(out, expected, atol=1e-6)
#
#     def test_box_blur_edge_padding(self):
#         # 2×2 image to test edge padding behavior
#         arr = np.array([[10, 20],
#                         [30, 40]], dtype=float)
#         img = ImageData(arr.copy())
#         # 3×3 box blur; edge padding replicates border pixels
#         blur = BoxBlurFilter(width=3, height=3)
#         out = blur.apply(img).get_array()
#         # Manually compute one corner (top-left):
#         # padded 3×3 region = [[10,10,20],
#         #                      [10,10,20],
#         #                      [30,30,40]]
#         # sum = 10*4 + 20*2 + 30*2 + 40*1 = 40+40+60+40 = 180; avg=180/9=20
#         self.assertAlmostEqual(out[0, 0], 20.0, places=6)
#
#     def test_chaining_with_dummy(self):
#         # Verify chaining: blur then dummy filter
#         arr = np.ones((5, 5), dtype=float) * 9
#         img = ImageData(arr.copy())
#         # A 3×3 blur of constant 9 remains 9; then dummy *2 → 18
#         chain = BoxBlurFilter(3, 3, next_filter=DummyFilter())
#         out = chain.apply(img).get_array()
#         self.assertTrue(np.allclose(out, 18.0))

def test_blur():
    # Insert your image path here
    image_path = "/Users/ronlevin/PycharmProjects/Lightricks_HA/tests/mona_lisa.jpg"

    # Load image
    img = ImageData.load(image_path)

    # Configure box blur dimensions
    width = 20  # e.g., change as needed
    height = 40  # e.g., change as needed

    # Apply BoxBlurFilter
    blur_filter = BoxBlurFilter(width=width, height=height)
    result = blur_filter.apply(img)

    # Display result
    result.show()

    # Optionally save result
    # output_path = "blurred_output.png"
    # result.save(output_path)
    # print(f"Blurred image saved to {output_path}")


if __name__ == "__main__":
    # unittest.main()
    test_blur()

#     # kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
#     img_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     img=ImageData(img_arr)
#     result = NoOpFilter().apply(img)
#     print(result.get_array())

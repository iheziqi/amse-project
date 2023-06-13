import os
from data_pipeline import my_data_pipeline
import unittest


class TestDataPipeline(unittest.TestCase):
    def test_data_pipeline(self):
        # Execute the data_pipeline function
        my_data_pipeline()

        # Check if data.sqlite file is created in the root directory
        self.assertTrue(os.path.isfile('../data.sqlite'))


if __name__ == '__main__':
    unittest.main()

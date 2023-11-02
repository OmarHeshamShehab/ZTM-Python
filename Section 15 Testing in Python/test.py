import unittest

import main


class TestMain(unittest.TestCase):
    def setup(self):  # to be run before each method
        print("about to run a function")

    def test_do_stuff(self):
        """hiiiiiiiiiiiiiiiiiiiii"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "wrong"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    def tearDown(self):  # to be run at the end of each function
        print("cleaning up function")


if __name__ == "__main__":
    unittest.main()

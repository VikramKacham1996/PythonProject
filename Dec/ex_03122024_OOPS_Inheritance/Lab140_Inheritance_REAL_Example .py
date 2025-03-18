class BaseTest:
    def open_browser(self):
        print("Starting the browser")

    def read_from_Excel(self):
        print("Reading from Excel")

    def close_browser(self):
        print("Closing the browser")


class TestCase1(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("Test case P1 Executed!!")
        self.read_from_Excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N1 Executed!!")
        self.close_browser()


class TestCase2(BaseTest):
    def test_2(self):
        self.open_browser()
        print("Test case P2 Executed!!")
        self.close_browser()


class TestCase3(BaseTest):
    def test_3(self):
        self.open_browser()
        print("Test case P3 Executed!!")
        self.close_browser()


# # Example usage
# if __name__ == "__main__":
#     # Test Case 1
#     t1 = TestCase1()
#     t1.test_positive()
#     t1.test_negative()
#
#     # Test Case 2
#     t2 = TestCase2()
#     t2.test_2()
#
#     # Test Case 3
#     t3 = TestCase3()
#     t3.test_3()

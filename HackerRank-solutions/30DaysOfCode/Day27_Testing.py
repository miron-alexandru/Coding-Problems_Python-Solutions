# Problem Link: https://www.hackerrank.com/challenges/30-testing/problem

# My Solution:
class TestDataEmptyArray:
    
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues:
    
    @staticmethod
    def get_array():
        return [2, 5, 8, 10, 1, 7, 3]
    
    @staticmethod
    def get_expected_result():
        return 4

class TestDataExactlyTwoDifferentMinimums:
    
    @staticmethod
    def get_array():
        return [2, 5, 8, 10, 1, 7, 1, 3]
    
    @staticmethod
    def get_expected_result():
        return 4

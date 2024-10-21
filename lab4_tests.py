import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[4,7,8], [9,10,11]]
        result = lab4.first_element(input)
        expected = [4, 9]
        self.assertEqual(expected, result)


    # Part 2
    def test_second_element_1(self):
        input = [(1,2),(3,4)]
        result = lab4.x_coordinates(input)
        expected = [1,3]
        self.assertEqual(expected, result)

    def test_second_element_2(self):
        input = [(5,6),(7,8),(9,10)]
        result = lab4.x_coordinates(input)
        expected = [5,7,9]
        self.assertEqual(expected, result)

    # Part 3
    def test_third_element_1(self):
        input = [(6,7),(-1,-2),(-5,1)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [(6,7)]
        self.assertEqual(expected, result)

    def test_third_element_2(self):
        input = [(8,9),(-10,-3),(-4,2), (3,-1), (5,6)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [(8,9), (5,6)]
        self.assertEqual(expected, result)

    # Part 4
    def test_fourth_element_1(self):
        input1 = (1,2)
        input2 = (4,6)
        result = lab4.distance(input1, input2)
        expected = round(5,2)
        self.assertEqual(expected, result)

    def test_fourth_element_2(self):
        input1 = (2, 3)
        input2 = (4, 5)
        result = lab4.distance(input1, input2)
        expected = round(2 * (2 ** 0.5), 2)
        self.assertEqual(expected, result)

    # Part 5
    def test_fifth_element_1(self):
        input1 = (2, 3)
        input2 = (4, 5)
        result = lab4.manhattan_distance(input1, input2)
        expected = 4
        self.assertEqual(expected, result)

    def test_fifth_element_2(self):
        input1 = (-2, 3)
        input2 = (4, -5)
        result = lab4.manhattan_distance(input1, input2)
        expected = 14
        self.assertEqual(expected, result)

    # Part 6
    def test_sixth_element_1(self):
        input = [(2,3),(4,5)]
        result = lab4.distance_all(input)
        expected = [13**0.5, 41**0.5]
        self.assertEqual(expected, result)

    def test_sixth_element_2(self):
        input = [(1,-3),(-4,6)]
        result = lab4.distance_all(input)
        expected = [10**0.5, 52**0.5]
        self.assertEqual(expected, result)

#if __name__ == '__main__':
#    unittest.main()

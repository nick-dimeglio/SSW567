# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(6, 10, 8), 'Right',
                         '6,10,8 is a Right triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles',
                         '3,3,4 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(99, 99, 88), 'Isoceles',
                         '3,3,4 is an Isosceles triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 6, 4), 'Scalene',
                         '3,6,4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(20, 29, 27), 'Scalene',
                         '3,6,4 is a Scalene triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200),
                         'Equilateral', '200,200,200 should be equilateral')

    def testNotTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 10),
                         'NotATriangle', '1,2,10 should not be a triangle')
        self.assertEqual(classifyTriangle(0, 0, 0),
                         'NotATriangle', '0,0,0 should not be a valid triangle.')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle("k", 2, 10),
                         'InvalidInput', 'k,2,10 should not be a valid input.')
        self.assertEqual(classifyTriangle(1.0, 2, 10),
                         'InvalidInput', '1.0,2,10 should not be a valid input.')
        self.assertEqual(classifyTriangle(201, 200, 201),
                         'InvalidInput', '201,200,201 should not be a valid input.')
        self.assertEqual(classifyTriangle(-1, 0, 0),
                         'InvalidInput', '-1,0,0 should not be a valid input.')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

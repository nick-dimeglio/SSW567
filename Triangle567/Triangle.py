# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


import heapq


def classify_triangle(side_one, side_two, side_three):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(side_one, int) and isinstance(side_two, int) and isinstance(side_three, int)):
        return 'InvalidInput'

    # ERROR: originally placed before check for valid integer inputs, potentially breakable code.
    # require that the input values be >= 0 and <= 200
    if side_one > 200 or side_two > 200 or side_three > 200:
        return 'InvalidInput'

    # error found where b was set to check for b<=b rather than b<= 0

    if side_one < 0 or side_two < 0 or side_three < 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # ERROR:found here where differences wer being checked rather than sums
    if ((side_one >= (side_two + side_three)) or
            (side_two >= (side_one + side_three)) or
            (side_three >= (side_one + side_two))):
        return 'NotATriangle'

    # now we know that we have a valid triangle

    # ADDED: code to order a,b, and c into smallest to largest respectively via heapification.
    # This is done to ensure that the correct side is being checked for the right angle.
    # It is also time efficient as heapification and sorting will only take O(n) time.
    # However, it is a bit redundant because there is a strict 3 side triangle requirement.
    # Still doing it out of good practice.
    sides = [side_one, side_two, side_three]
    heapq.heapify(sides)
    side_one = heapq.heappop(sides)
    side_two = heapq.heappop(sides)
    side_three = heapq.heappop(sides)
    # ERROR: found here, not checking other cases for equilateral
    if side_one == side_two and side_three == side_one and side_two == side_three:
        return 'Equilateral'
    # ERROR: found here, multiplying not using exponent.
    if ((side_one ** 2) + (side_two ** 2)) == (side_three ** 2):
        return 'Right'
    if (side_one != side_two) and (side_two != side_three) and (side_one != side_two):
        return 'Scalene'
    return 'Isoceles'

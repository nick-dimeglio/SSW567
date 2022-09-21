# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


import heapq


def classifyTriangle(a, b, c):
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
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # ERROR: originally placed before check for valid integer inputs, potentially breakable code.
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # error found where b was set to check for b<=b rather than b<= 0

    if a < 0 or b < 0 or c < 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # ERROR:found here where differences wer being checked rather than sums
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle

    # ADDED: code to order a,b, and c into smallest to largest respectively via heapification.
    # This is done to ensure that the correct side is being checked for the right angle.
    # It is also time efficient as heapification and sorting will only take O(n) rather than O(nlogn) time.
    # However, it is a bit redundant because there is a strict 3 side triangle requirement.
    # Still doing it out of good practice.
    sides = [a, b, c]
    heapq.heapify(sides)
    a = heapq.heappop(sides)
    b = heapq.heappop(sides)
    c = heapq.heappop(sides)
    # ERROR: found here, not checking other cases for equilateral
    if a == b and c == a and b == c:
        return 'Equilateral'
    # ERROR: found here, multiplying not using exponent.
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'

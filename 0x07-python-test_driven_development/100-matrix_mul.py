#!/usr/bin/python3

"""
This module defines a function to multiply two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list): The first matrix as a list of lists.
        m_b (list): The second matrix as a list of lists.

    Returns:
        list: The resulting matrix as a list of lists.

    Raises:
        TypeError: If either m_a or m_b is not a list or a list of lists, or if an element in either matrix
                   is not an integer or a float, or if the rows of either matrix are not of the same size.
        ValueError: If either m_a or m_b is empty, or if the matrices cannot be multiplied.

    """
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if m_a == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(val, (int, float)) for row in m_a for val in row) or not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply the matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = 0
            for k in range(len(m_b)):
                val += m_a[i][k] * m_b[k][j]
            row.append(val)
        result.append(row)
    return result

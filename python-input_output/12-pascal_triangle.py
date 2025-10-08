#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list of lists of int: Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # First element

        # Compute middle elements as sum of two elements from previous row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last element
        triangle.append(row)

    return triangle

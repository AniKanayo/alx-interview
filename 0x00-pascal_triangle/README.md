# Interview Question: Pascal's Triangle

This interview question focuses on generating Pascal's Triangle up to a given number of rows. The solution should generate the triangle and print it in the required format.

## Problem Description

Pascal's Triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it. The triangle starts with a single 1 at the top and continues to build subsequent rows based on the rule.

Your task is to write a function that generates Pascal's Triangle up to a given number of rows and prints it in the following format:

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
...
```

## Implementation

You need to implement the function `pascal_triangle(n)` that takes an integer `n` as input and returns a 2D list representing Pascal's Triangle with `n` rows. Each row of the triangle should be a list containing the elements of that row.

The algorithm to generate Pascal's Triangle involves iterating over the rows and using the previous row to calculate the current row. The first and last elements of each row are always 1, while the elements in between are calculated as the sum of the corresponding elements from the previous row.

## Example

```python
result = pascal_triangle(5)
for row in result:
    print(' '.join(str(num) for num in row))
```

Output:

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

## Constraints

- The input `n` will be a positive integer.
- The output should be printed in the specified format.

## Discussion

This question assesses the candidate's understanding of generating Pascal's Triangle and their ability to implement the algorithm correctly. It tests their knowledge of nested loops, array manipulation, and string formatting.

Candidates should demonstrate their understanding of the problem, provide a well-structured solution, and handle edge cases appropriately.

## Follow-up Questions

1. Can you optimize the solution to use less memory?
2. How would you handle larger values of `n` efficiently?

---

Feel free to modify and customize this README file according to your specific requirements. You can add sections for input/output examples, explanations of the algorithm, and further discussions. Make sure to provide clear instructions and details to help the interviewee understand and solve the problem effectively.

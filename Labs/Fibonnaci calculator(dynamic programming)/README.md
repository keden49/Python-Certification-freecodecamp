# Build an Nth Fibonacci Number Calculator

## Objective
Fulfill the user stories below and get all the tests to pass to complete the lab.

## User Stories:

- You should create a function named fibonacci.
- You should define a list named sequence within the fibonacci function, and it should be initialized with the values [0, 1].
- The fibonacci function should accept one parameter, a positive integer n.
- Calling fibonacci(n) should use a dynamic programming approach to compute and return the n-th number from the Fibonacci sequence, where each number is the sum of the two preceding numbers. :contentReference[oaicite:0]{index=0}
- Each computed number at the position n in the Fibonacci sequence should be stored in the sequence list at index n - 1.

## Tests:

1. You should have a function named fibonacci.
2. Your fibonacci function should take a single parameter.
3. You should have a list named sequence within the fibonacci function initialized to [0, 1].
4. fibonacci(0) should return 0.
5. fibonacci(1) should return 1.
6. fibonacci(2) should return 1.
7. fibonacci(3) should return 2.
8. fibonacci(5) should return 5.
9. fibonacci(10) should return 55.
10. fibonacci(15) should return 610.
11. You should not use recursion in your code.

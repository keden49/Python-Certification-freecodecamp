# -*- coding: utf-8 -*-
def fibonacci(n)

  # initializing sequence

  sequence = [0, 1]

  for i in range(2,n+1):
    # next number in a sequence is determined by the two preceding numbers before it
    next_no  = sequence[i-1] + sequence[i-2]
    sequence.append(next_no)

  return sequence[n]

# logic 2
'''
Space efficient
only stores last 2 values
'''

def fibonacci(n):

  # initializing sequence

  sequence = [0, 1]

  prev2,prev1 = sequence #unpacking list

  # storing values of only the last 2 previous values in the sequence
  # to be memory efficient

  if n == 0:
    return prev2

  for _ in range(2,n+1):
    next_no = prev1 + prev2
    prev2 = prev1
    prev1 = next_no

  return prev1 #

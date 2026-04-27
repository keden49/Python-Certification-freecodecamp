'''
This implementation aims to solve some of the inefficiencies the third algorithm had'''
def quicksort(array):

  if len(array) <= 1:
    return array

  mid = len(array)//2
  pivot = array[mid]#use middle element as pivot to avoid redundacy when list is already sorted

  #list comprehensions are mre efficient as they are implemented in C

  left_array = [x for x in array if x < pivot]
  middle_array = [x for x in array if x ==pivot] #middle array to avoid redudancy when list has multiple duplicates
  right_array = [x for x in array if x > pivot]

  return quicksort(left_array) + middle_array + quicksort(right_array)


  '''
  Observations:
  Merge sort algorithm is starts soting once it reaches base case making
  its way up, while quick sort sorts while making its way down such that when it reaches base case their is nothing to sort
  ''' 
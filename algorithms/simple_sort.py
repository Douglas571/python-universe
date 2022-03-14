def selection_sort(array):
  A = array.copy()
  sorted_A = []

  for _ in range(len(A)):
    e = min(A)
    sorted_A.append(e)
    A.pop(A.index(e))

  return sorted_A

def swap(A, i, j):
  temp = A[i]
  A[i] = A[j]
  A[j] = temp

  return A

def insertion_sort(array):
  A = array.copy()

  for i in range(2, len(A)):
    j = i
    while (A[j] < A[j-1] and j > 0):
      swap(A, j, j-1)
      j -= 1

  return A

A     = [4, 9, 4, 10, 7, 2, 1, 3, 5, 6, 8]
exp_A = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
print(f'the sorted array {A}\nshould be {exp_A}')

B = selection_sort(A)
assert B == exp_A
print(f'selection sort: {B}')

C = insertion_sort(A)
assert C == exp_A
print(f'insertion sort: {C}')
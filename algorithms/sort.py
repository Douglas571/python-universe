from collections import deque
import math

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

def merge(A, low, mid, top):
  i = 0

  buffer1 = deque(S[low:mid+1])
  buffer2 = deque(S[mid:top])

  print(f'buffer1={buffer1}')
  print(f'buffer2={buffer2}')
  i = low
  while not (len(buffer1) == 0 or len(buffer2) == 0):

    if buffer1[0] <= buffer2[0]:
      S[i] = buffer1.popleft()
      i += 1
    else:
      S[i] = buffer2.popleft()
      i += 1

  while not len(buffer1) == 0:
    S[i] = buffer1.popleft()
    i += 1

  while not len(buffer2) == 0:
    S[i] = buffer2.popleft()
    i += 1    

  print(f'final merge: {S}')



def mergesort(S, low, top):
  # si hay para dividir:
    # hacer mergesort con la mitad inferior
    # hacer mergesort con la mitad superior
    # hacer merge con las mitades

  print(f'\niter -> low={low}, top={top}')
  if low < top:
    print(f'low < top => {low} < {top} => {(low < top)}')
    mid = math.floor((low + top) / 2)

    print(f'1th, low={low}, mid={mid}')
    mergesort(S, low, mid)

    print(f'2th, mid={mid}, mid+1={(mid+1)}, top={top}')
    mergesort(S, mid+1, top)

    merge(S, low, mid, top)

import unittest

class TestCase(unittest.TestCase):
  def test_one(self):
    A   = [4, 9, 4, 10, 7, 2, 1, 3, 5, 6, 8]
    exp = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]

    ssr = selection_sort(A)
    self.assertEqual(ssr, exp)

    isr = insertion_sort(A)
    self.assertEqual(isr, exp)

    d = deque(A)
    print(f'1th of deque = {d[0]}')

    msr = mergesort(A, 0, len(A))
    self.assertEqual(msr, exp)

if __name__ == '__main__':
  unittest.main()
# https://www.geeksforgeeks.org/bubble-sort/
# https://www.geeksforgeeks.org/python-program-for-merge-sort/

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

  for i in range(1, len(A)):
    j = i
    while (A[j] < A[j-1] and j > 0):
      swap(A, j, j-1)
      j -= 1

  return A

def merge(A, low, mid, top):
  # print(f'merg: low={low}, mid={mid}, top={top}')
  buf_a = []
  buf_b = []

  i = low
  while i <= mid:
    # print(f'low i={i}')
    buf_a.append(A[i])
    i += 1

  i = mid + 1
  while i <= top:
    buf_b.append(A[i])
    i += 1

  # print(f'buf_a={buf_a}')  
  # print(f'buf_b={buf_b}')

  i = low
  while not (len(buf_a) == 0 or len(buf_b) == 0):
    if buf_a[0] <= buf_b[0]:
      A[i] = buf_a.pop(0)
      i += 1

    else:
      A[i] = buf_b.pop(0)
      i += 1

  while not len(buf_a) == 0:
    A[i] = buf_a.pop(0)
    i += 1    

  while not len(buf_a) == 0:
    A[i] = buf_b.pop(0)
    i += 1

  # print(f'buf_a={buf_a}')  
  # print(f'buf_b={buf_b}')

  # print(f'final A={A}')
  s = A

def mergesort(A, low, top, S=None):
  if not S: S = A.copy()
  if S: A = S

  if low < top:
    mid = math.floor((low + top) / 2)
    # print(f'mergesort: low={low}, mid={mid}, top={top}, A = {A}')
    mergesort(A, low, mid, S)
    # print('sencond part')
    mergesort(A, mid+1, top, S)
    merge(A, low, mid, top)

  return S

import unittest

class TestCase(unittest.TestCase):
  def test_one(self):
    A   = [3, 1, 5, 2, 4]
    exp = sorted(A)

    ssr = selection_sort(A)
    self.assertEqual(ssr, exp)

    isr = insertion_sort(A)
    self.assertEqual(isr, exp)

    msr = mergesort(A, 0, len(A)-1)
    self.assertEqual(msr, exp)

if __name__ == '__main__':
  unittest.main()
from collections import deque
import timeit


def test_list():
  l = []

  for n in range(1000):
    l.append(n)

  while len(l) > 0:
    l.pop(0)

  return 0

def test_dequeue():
  
  l = deque([])

  for n in range(1000):
    l.append(n)

  while len(l) > 0:
    l.popleft()

  return 0

times = 2000


def test_list_2():
  l = [ 0 for n in range(1000)]

  for n in range(1000):
    l[n] = n

  for n in l:
    a = n

print('init list test 2')
list_res_2 = timeit.timeit(test_list_2, number=times)
print(f'results = {list_res_2}')

print('init list test')
list_res = timeit.timeit(test_list, number=times)

print('init deque test')
deque_res = timeit.timeit(test_dequeue, number=times)

print(f'results:\n  list={list_res}ms\n  deque={deque_res}ms')

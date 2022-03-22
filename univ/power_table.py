# Calculate the power table of a number

import sys

def inquire():
  try:
    n = input("[?] what's the number (defualt=2): ")
    i = input("[?] what's the index (default=7): ")

    if n == '': n = 2
    else: n = int(n)

    if i == '': i = 7
    else: i = int(i)

  except ValueError:
    print('ValueError: Write correct integuers\n')
    return inquire()

  return n, i

def parse_argv():
  print(sys.argv)
  try:
    n = int(sys.argv[1])
    i = int(sys.argv[2])
  except ValueError:
    print('ValueError: Incorrect input type\n')
    return inquire()

  return n, i

def get_input():
  if len(sys.argv) < 3:
    return inquire()
  return parse_argv()

def main():
  print('[Sofware Info] Display a power table of a given number\n')

  n, i = get_input()

  print(f'[Result] The power table of {n} from 0 to {i} is:')
  for i in reversed(range(i+1)):
    res = pow(n, i)
    print(f'{n:>2}^{i:<2} = {res}')

if __name__ == '__main__':
  main()
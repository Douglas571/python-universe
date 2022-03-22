# Tranforming binary numbers to decimal

def dec_to_bin(n):
  if n < 0: return

  res = [ '0' for z in range(8)]
  for i in reversed(range(8)):
    p = pow(2, i)

    if n - p >= 0:
      n -= p
      res[i] = "1"

  res = '0b' + ''.join(reversed(res))

  return res

def main():
  n = 255
  res = dec_to_bin(n)

  print(f'n={n}, bin={res}')
  assert res == '0b11111111'

  n = 64
  res = dec_to_bin(n)

  print(f'n={n}, bin={res}')
  assert res == '0b01000000'

  n = 63
  res = dec_to_bin(n)

  print(f'n={n}, bin={res}')
  assert res == '0b00111111'

if __name__ == '__main__':
  main()

  res = ''
  n = 8
  c = 0
  while not c in [0, 1] and not n in [0, 1]:
    n -= 2 
    c += 1

    print(f'c={c}, n={n}')

    if n in [0, 1]:
      n = c
      res = res + str(n)
    

  print(f'res={res}')
import sys

def process(l):
  s = l
  s_code = ord(s)
  s_bin = bin(s_code)  

  return s, s_code, s_bin

def main():
  word = 'example'
  if len(sys.argv) > 1:
    word = sys.argv[1]

  for l in word:
    s, c, b = process(l)
    print(f'"{s}" => {c:>3} => {b}')

if __name__ == '__main__':
  main()
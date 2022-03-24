import sys

def inquire():
  word = input('[?] Pass me a word: ')
  return word

def parse_argv():
  word = sys.argv[1]
  return word

def get_input():
  if len(sys.argv) > 1: 
    return parse_argv()
  return inquire()

def process(l):
  s = l
  s_code = ord(s)
  s_bin = bin(s_code)  

  return s, s_code, s_bin

def main():
  print('[Software Info] Convert a word to ASCII code and Binary\n')
  word = get_input()

  print('{:^8}-{:^7}-{:^9}'.format("Letter", "ASCII", "Binary"))
  print('-------------------------')
  for l in word:
    s, c, b = process(l)
    s = '"' + s + '"'
    b = b[2:]
    print('{:^8}|{:^7}|{:^9}'.format(s, c, b))

if __name__ == '__main__':
  main()
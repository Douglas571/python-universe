import sys

def main():
  if len(sys.argv) > 1:
    word = sys.argv[1]

if __name__ == '__main__':
  main()

  a = 'a'
  help(chr)
  a_code = chr(a)
  help(int)
  # a_bin = int(a_code, 2)
  # print(f'"a" => {a_code} => {a_bin}')
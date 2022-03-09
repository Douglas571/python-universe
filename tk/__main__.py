from quotes_lib import *

def main():
  quote, author = get_quote_of_the_day()
  print(f'"{quote}" by {author}')

if __name__ == "__main__":
  main()
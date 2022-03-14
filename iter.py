def get_directions(i, j):
  yield (i-1, j, 'up')
  yield (i+1, j, 'down')
  yield (i, j+1, 'rigth')
  yield (i, j-1, 'left')
  yield (i-1, j-1, 'left_up')
  yield (i+1, j-1, 'left_down')
  yield (i-1, j+1, 'rigth_up')
  yield (i+1, j+1, 'rigth_down')

class Directions:
  def __init__(self, i, j):
    up = (i-1, j)
    down = (i+1, j)
    rigth = (i, j+1)
    left = (i, j-1)
    left_up = (i-1, j-1)
    left_down = (i+1, j-1)
    rigth_up = (i-1, j+1)
    rigth_down = (i+1, j+1)

    self.directions = (
      up, rigth_up, rigth, rigth_down, 
      down, left_down, left, left_up
    )

    self.current = -1

  def __iter__(self):
    return self

  def __next__(self):
    self.current += 1
    if self.current < len(self.directions):
      return self.directions[self.current]

    raise StopIteration

def main():
  for i, j in Directions(0, 0):
    print(f'{i}, {j}')

  print('second')
  for i, j, name in get_directions(0, 0):
    print(f'{name}: {i}, {j}')

main()
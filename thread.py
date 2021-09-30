import threading
import sys
from time import sleep

class Counter:
    def __init__(self):
        self.counter = 0
        self.c_lock = threading.Lock()

    def up(self):

        couter = 0

        self.counter += 1
        print(f'up {self.counter}')

        return couter

    def get(self):

        return self.counter



def print_n_times(n_times, counter, event):
    ct = threading.current_thread()
    mt = threading.main_thread()

    if ct.name != mt.name:
        event.wait()
    
    for time in range(n_times):
        counter.up()
        print(f'{ct.name}: {time}')
        sleep(1)

    event.set()    


def main():

    times_to_print = int(sys.argv[1])
    COUNTER = Counter()

    cont = threading.Event()

    printer = threading.Thread(target=print_n_times,
                               args=(times_to_print, COUNTER, cont),
                               name='printer',
                            )
    printer.start()

    #timer = threading.Timer(10.0, print_n_times, args=(times_to_print, COUNTER))
    #timer.start()

    print_n_times(5, COUNTER, cont)

    print('finished')

    def get_count(c):
        print(f'{c.get()} COUNTS')

    timer = threading.Timer(5.0, get_count, args=(COUNTER,))
    timer.start()

if __name__ == '__main__':
    main()
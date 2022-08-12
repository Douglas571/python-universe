import modlA

import time

def main():
    dic = { "name": "douglas" }
    print(modlA.hello(dic))

    start = time.time()

    time.sleep(2.3)
    end = time.time()

    msg = 'total time is: '
    ttl = end - start
    print('%s %4.2fsec'%(msg, ttl))

if __name__ == '__main__':
    main()
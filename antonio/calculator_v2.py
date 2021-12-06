"""
A calculator writed in python

"""

def main():
    operations = {
        '+': { 'name': 'Addition',     'fun': add },
        '-': { 'name': 'Substraction', 'fun': sub },
        'x': { 'name': 'Product',      'fun': pro },
        '/': { 'name': 'Divition',     'fun': div }
    }
    
    register = {
        'a': 0,
        'b': 0,

        'result': None
    }

    keep_work = True
    while keep_work:
        operation = input('Choice a operation (+, -, x, /): ')
        
        try:
            op_name = operations[operation]['name']
            print(f'--- {op_name} ---')

        except KeyError as err:
            print(f'{err} is an invalid operation')
            print()

        else:
            if register['result'] != None:
                print('use _ to reffer the last operations did\n')

            a = input('Numb A: ')
            if a == '_':
                a = register['result']
            else:
                a = float(a)

            b = float(input('Numb B: '))

            result = operations[operation]['fun'](a, b)

            register['a'] = a
            register['b'] = b
            register['result'] = result

            print(f'the result is: {result}')
        
        keep_work = input('Keep working? (y/n): ')
        if keep_work == 'y':
            keep_work = True
        else:
            keep_work = False

        print('')
    print('Good Bye')

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def pro(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == '__main__':
    main()
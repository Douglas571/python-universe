# A calculator writed in python
# NOTA: La mayoria del código está en ingles 
# porque ya lo había hecho antes, así que copie
# y pegue todo en una clase "Calculator".

class Calculator:
    def __init__(self):
        self.operations = {
            '+': { 'name': 'Addition',     'fun': self.add },
            '-': { 'name': 'Substraction', 'fun': self.sub },
            'x': { 'name': 'Product',      'fun': self.pro },
            '/': { 'name': 'Divition',     'fun': self.div }
        }
       
        self.register = {
            'a': 0,
            'b': 0,

            'result': None
        }

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def pro(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def run(self):
        keep_work = True
        while keep_work:
            operation = input('Choice a operation (+, -, x, /): ')
            
            try:
                op_name = self.operations[operation]['name']
                print(f'--- {op_name} ---')

            except KeyError as err:
                print(f'{err} is an invalid operation')
                print()

            else:
                if self.register['result'] != None:
                    print('use _ to reffer the last operations did\n')

                a = input('Numb A: ')
                if a == '_':
                    a = self.register['result']
                else:
                    a = float(a)

                b = float(input('Numb B: '))

                result = self.operations[operation]['fun'](a, b)

                self.register['a'] = a
                self.register['b'] = b
                self.register['result'] = result

                print(f'the result is: {result}')
            
            keep_work = input('Keep working? (y/n): ')
            if keep_work == 'y':
                keep_work = True
            else:
                keep_work = False

            print('')
        print('Good Bye')
    

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
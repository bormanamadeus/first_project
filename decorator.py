#! python

def Main():
    def decor(func):
        print('function: ', func)
        return func

    @decor
    def F():
        print('F job')

    F()

if __name__ == '__main__':
    Main()

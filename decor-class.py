#! python

def Main():
    x = C(6, 7)
    print(x.attr)

def decorator_class(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper

class C:
    def __init__(self, x, y):
        self.attr = 'spam'

if __name__ == '__main__':
    Main()

#! python
# coding=utf-8

def Main():
    spam(1, 2, 4) 
    spam(a=4, b=5, c=6)

    eggs(2, 16)
    eggs(4, y=4)

    sum(10, 20)
    sum(30, b=100)

    sum2(100, 200)
    sum2(300, b=1000)

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

def tracerfunc(func):
    calls = 0
    def tracer(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return tracer

def tracer_func_atribut(func):
    def tracer(*args, **kwargs):
        tracer.calls += 1
        print('call %s to %s' % (tracer.calls, func.__name__))
        return func(*args, **kwargs)
    tracer.calls = 0
    return tracer

@tracer
def spam(a, b, c):
    print(a + b + c)

@tracer
def eggs(x, y):
    print(x ** y)

@tracerfunc
def sum(a, b):
    print(a + b)

@tracer_func_atribut
def sum2(a, b):
    print(a + b)


if __name__ == '__main__':
    Main()

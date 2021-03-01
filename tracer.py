#! python

def Main():
    @tracer
    def spam(a, b, c):
        print('spam: %s %s %s' % (a, b, c))

    class Person:
        @tracer
        def giveRaise(self, percent):
            print('percent: ', percent)

    spam(10, 'a', 'Help')

    p = Person()
    p.giveRaise(100)
    
    spam(20, 'm', 'h')
    p.giveRaise(200)
   
class tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' %(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)

class tracer2(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' %(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper 


if __name__ == '__main__':
    Main()

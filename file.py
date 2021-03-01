#! python
import keyboard

def Main():
    print('Enter the path to the file: ', end = '')
    filepath = input() 

    keyboard.hook(showfile(filepath))

def showfile(filepath):
    def hookfunc(key):
        file = open('textfile', 'r', encoding = 'utf-8')
        st = file.read()
        print(st)
        file.close()

    return hookfunc


if __name__ == '__main__':
    Main()

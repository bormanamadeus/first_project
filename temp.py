#! python
def Main():
    s = bytearray(b'Hello manH')

    print(s)

    printbyte(s)

    s = s + b'!#'

    print('-----------------------')

    printbyte(s)
    print(printbyte.__annotations__)


def printbyte(st: str) -> None:
    for value in st:
        print(value, end = '')
        print(chr(value))

    
if __name__ == '__main__':
    Main()

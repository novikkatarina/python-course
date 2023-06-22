def prompt():
    print('1 import')
    print('2 export')

    x = input('what to do?\n')
    return x


def prompt_import():
    return input('enter filename\n')


def prompt_export():
    return input('enter format\n')

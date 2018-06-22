from farf import *

if __name__ == '__main__':
    arg1 = './dummydir/'
    arg2 = input('\nfind what?')
    arg3 = input('\nreplace with what?')
    try:
        if arg1 in ('--help', '-help', '/help', 'help'):
            farfer.printhelp()
            quit()
    except IndexError:
        print('arg1 is blank (no search directory submitted). \nAborting.')
        quit()
    try:
        foo = arg2
    except IndexError:
        print('arg2 is blank (no find string submitted). \nAborting.')
        quit()
    try:
        foo = arg3
    except IndexError:
        print(
            'arg3 is blank (no replace string submitted). \n Are you sure you want to blank out the file name?\n(y/n)')
        answer = str(input())
        if answer in 'y':
            arg3 = ''
        else:
            quit()

    farfout = []
    ourFarfer = farfer(arg1, arg2, arg3)
    ourFarfer.farf()

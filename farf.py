from os import walk, rename, path, makedirs
from sys import argv
from re import sub
import pickle


# FaRF: Find and Rename Files
# A useful and dangerous tool for
#  find-replacing strings in filenames within a drectory.
#
# By default there's a confirm in-place for renaming.
# modify the code if you really want to make batch jobs.
class farfer():
    def __init__(self, pth, fnd, rpl):
        self.mode = ''
        self.farfin = []
        self.farfout = []
        self.pathname = pth
        self.search_string = fnd
        self.replace_with = rpl

    def farf(self):
        farfout = []
        for root, dirs, files in walk(self.pathname, topdown=False):
            for file in files:
                if self.search_string in file:
                    print('Old Name: ' + str(self.search_string) + ' in ' + str(file) + ' with ' + str(self.replace_with))
                    print('New Name: ' + sub(self.search_string, self.replace_with, file))
                    allow = input('Allow this operation? (y/n)')
                    if str(allow) in 'y':
                        farfout.append({self.search_string, file, self.replace_with})
                        rename(path.join(root, file), sub(self.search_string, self.replace_with, path.join(root, file)))

    # For saving farfs out to a file for reversing farfs
    # Pickle format: a list of these sets: [{self.search_string, file, self.replace_with},{..., ..., ...}...]
    # (insecure right now, the file can be pickled in without auth. ) TODO: add encryption of farfouts?
    def farfoutput(self):
        filename = input("save farf output as:")
        savefolder = "./farfoutput/"
        filepath = savefolder + filename + '.farf'
        if not path.isdir(savefolder):
            makedirs(savefolder)
        with open(filepath, 'wb') as f:
            pickle.dump(self.farfout, f, -1)
        return

    # TODO: Make unfarf
    def unfarf(self):
        pass

    def printhelp(self):
        print('FaRF - Find and Rename Files - Colin Burke 2018\n'
              'USAGE:\n'
              'farf.py <path:str> <self.search_string:str> <self.replace_with:str>\n'
              'Ex: farf.py ../dummydir foo bar\n'
              )

if __name__ == '__main__':
    try:
        if argv[1] in ('--help', '-help', '/help', 'help'):
            farfer.printhelp()
            quit()
    except IndexError:
        print('argv[1] is blank (no search directory submitted). \nAborting.')
        quit()
    try:
        foo = argv[2]
    except IndexError:
        print('argv[2] is blank (no find string submitted). \nAborting.')
        quit()
    try:
        foo = argv[3]
    except IndexError:
        print('argv[3] is blank (no replace string submitted). \n Are you sure you want to blank out the file name?\n(y/n)')
        answer = str(input())
        if answer in 'y':
            argv[3] = ''
        else:
            quit()

    farfout = []
    ourFarfer = farfer(argv[1], argv[2], argv[3])
    ourFarfer.farf()

import sys
import os

def getFilenames(path):
    files = []

    for r, d, f in os.walk(path):
        for name in f:
            files.append(os.path.join(r, name))

    return files

def main():
    
    files = getFilenames('./20_newsgroups/')
             
    print files
    print len(files)
    exit()


if __name__ == '__main__':
    main()



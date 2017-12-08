import sys
import os

def getFilenames(path):
    files = {}
    
    for r, d, f in os.walk(path):
        for name in f:
            files[os.path.join(r,name)] = r

    return files

def stripchars(line):
    # Characters to strip
    chars = ['.', ' ', '\n', '--', '!']

    for c in chars:
        line = line.replace(c, ' ')

    return line


def getWordcount(filename):
    filereader = open(filename, 'r')

    words = {}

    for line in filereader:
        line = stripchars(line).split(' ')
        for word in line:
            word = word.lower()
            if word != '':
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1


def main():
    
    files = getFilenames('./20_newsgroups/')
    
    print len(files)
    getWordcount(files.popitem()[0])
    exit()


if __name__ == '__main__':
    main()



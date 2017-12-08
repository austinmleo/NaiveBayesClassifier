import sys
import os

def getFilenames(path):
    files = {}
    
    for r, d, f in os.walk(path):
        filesInDir = []
        for name in f:
            filesInDir.append(os.path.join(r,name))

        files[r] = filesInDir
    
    return files

def stripchars(line):
    # Characters to strip
    chars = ['.', ' ', '\n', '--', '!']

    for c in chars:
        line = line.replace(c, ' ')

    return line


def getWordcount(filename):
    words = {}
    
    filereader = open(filename, 'r')

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
    print files
    print len(files)

    allClasses = list(files.keys())
    classifier = {}

    testData = []
    correctResults = []


    for classification in files:
        breakCount = 0
        for f in files[classification]:
            wordCounts = getWordCount(f)

            if breakCount < 800:
                classifier = train(wordCount, classifier, classification, allClasses)
            else:
                testData.append(wordCounts)
                correctResults.append(classification)
            
            breakCount += 1


    for t in testData:
        classification = test(t)

  
    exit()


if __name__ == '__main__':
    main()



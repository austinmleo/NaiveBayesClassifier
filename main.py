import sys
import os

from train import *
from test import *

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


def getWordCount(filename):
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

    return words


def compare(test, true):
    size = len(test)
    correct = 0

    for i in range(size):
        correct += 1 if test[i] == true[i] else 0

    return float(correct) / size




def main():
    
    print "Getting file names..."
    files = getFilenames('./20_newsgroups/')

    allClasses = list(files.keys())
    classifier = {}

    testData = []
    correctResults = []


    for classification in files:
        print
        print "Training class: {}...".format(classification)
        breakCount = 0
        for f in files[classification]:
            wordCounts = getWordCount(f)

            if breakCount < 800:
                classifier = train(wordCounts, classifier, classification, allClasses) 
            else:
                if breakCount == 800:
                    print "Tracking test data for this class..."
                testData.append(wordCounts)
                correctResults.append(classification)
            
            breakCount += 1


    testResults = []

    print
    size = len(testData)
    for i in range(size):
        sys.stdout.write("Testing data... [%d%%]    \r" % (float(i) / size))
        sys.stdout.flush()
        t = testData[i]
        testResults.append(test(t, classifier, allClasses))
        
    print
    print "Analyzing results..."
    accuracy = compare(testResults, correctResults)
    print "Accuracy: {0:.4f}".format(accuracy)

  
    exit()


if __name__ == '__main__':
    main()



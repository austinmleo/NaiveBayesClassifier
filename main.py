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
    chars = ['.', '\n', '!', '<', '>', '[', ']', '@', '(', ')', '-', ':', '=', '?', '*']

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
            if len(word) > 5:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

    return words


def compare(test, true):
    size = len(test)
    results = {}
    counts = {}

    overall = 0

    for i in range(size):
        correct = 1 if test[i] == true[i] else 0
        try:
            results[true[i]] += correct
        except KeyError:
            results[true[i]] = correct

        overall += correct

        try:
            counts[true[i]] += 1
        except KeyError:
            counts[true[i]] = 1


    for classification in results.keys():
        results[classification] *= 100./counts[classification]

    accuracy = (100.*overall) / size

    return results, accuracy




def main():
    print "Getting file names..."
    files = getFilenames('./20_newsgroups/')

    allClasses = list(files.keys())
    classifier = {}

    testData = []
    correctResults = []

    print
    for classification in files:
        sys.stdout.write("\x1b[KTraining class: %s    \r" % (classification))
        sys.stdout.flush()
        breakCount = 0
        for f in files[classification]:
            wordCounts = getWordCount(f)

            if breakCount < 800:
                classifier = train(wordCounts, classifier, classification, allClasses) 
            else:
                testData.append(wordCounts)
                correctResults.append(classification)
            
            breakCount += 1

    testResults = []

    print
    print "Counting totals..."

    wordTotals = {}
    for word in classifier.keys():
        wordTotals[word] = sum(classifier[word].values())

    classTotals = {}
    for c in allClasses:
        classTotals[c] = getClassTotal(c, classifier)

    grandTotal = sum(wordTotals.values())

    size = len(testData)
    for i in range(size):
        progress = 100 * float(i) / size
        sys.stdout.write("Testing data... [%d%%]    \r" % (progress))
        sys.stdout.flush()

        t = testData[i]
        classification, probability = test(t, classifier, allClasses, \
                wordTotals, classTotals, grandTotal)
        testResults.append(classification)
        
    print
    print "Analyzing results..."
    print
    results, accuracy = compare(testResults, correctResults)

    for classification in results.keys():
        print "Class: {}".format(classification)
        print "Accuracy: {0:.4f}".format(results[classification])
        print

    print "Overall accuracy: {0:.4f}".format(accuracy) 
    exit()


if __name__ == '__main__':
    main()



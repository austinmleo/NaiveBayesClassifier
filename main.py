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
    chars = ['.', '\n', '!', '<', '>', '[', ']', '(', ')', '-', ':', '=', '?', '*']

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
            if len(word) > 10:
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
    count = 0

    for i in range(size):
        for c in test[i]:
            correct = 1 if c in true[i] else 0
            try:
                results[c] += correct 
            except KeyError:
                results[c] = correct 
            
            overall += correct
            count += 1
        
        for c in true[i]:
            try:
                counts[c] += 1
            except KeyError:
                counts[c] = 1


    for classification in results.keys():
        results[classification] *= 100./counts[classification]

    accuracy = (100.*overall) / count

    return results, accuracy




def main():
    print "Getting file names..."
    files = getFilenames('./20_newsgroups/')

    allClasses = []
    for f in files.keys():
        classes = f.split('/')[-1].split('.')
        for classification in classes:
            allClasses.append(classification)

    allClasses = set(allClasses)

    classifier = {}

    testData = []
    correctResults = []

    print
    for directory in files:
        classifications = directory.split('/')[-1].split('.')
        
        sys.stdout.write("\x1b[KTraining classes: %s    \r" % (classifications))
        sys.stdout.flush()

        breakCount = 0
        for f in files[directory]:
            wordCounts = getWordCount(f)

            if breakCount < 800:
                classifier = train(wordCounts, classifier, classifications, allClasses) 
            else:
                testData.append(wordCounts)
                correctResults.append(classifications)
            
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
        classifications = test(t, classifier, 3, allClasses, \
                wordTotals, classTotals, grandTotal)

        classes = []
        for rank in classifications:
            classes.append(rank[0])

        testResults.append(classes)
        
    print
    print "Analyzing results..."
    print
    results, accuracy = compare(testResults, correctResults)

    for classification in results.keys():
        print "Class: {}".format(classification)
        print "Accuracy: {0:.4f}".format(results[classification])
        print

    print "Overall accuracy: {0:.4f}".format(accuracy)
    print "Words detected: {}".format(len(classifier.keys()))
    exit()


if __name__ == '__main__':
    main()



def test(data, classifier, allClasses):
    bestClass = allClasses[0]
    bestProb = 0

    wordTotals = {}
    for word in classifier.keys():
        wordTotals[word] = sum(classifier[word].values())

    grandTotal = sum(wordTotals.values())

    for c in allClasses:
        classTotal = getClassTotal(c, classifier)

        for word in data:
            try:
                wordTotal = wordTotals[word]
            except KeyError as e:
                continue

            prob = classifier[word][c]*(1/wordTotal)*(classTotal/grandTotal)

            if prob > bestProb:
                bestProb = prob
                bestClass = c

    return bestClass, bestProb


def getClassTotal(c, classifier):
    total = 0
    for word in classifier.keys():
#        print "Word: {}".format(word)
#        print "Class: {}".format(c)
#        print "Classifier: {}".format(classifier[word])
        total += classifier[word][c]

    return total

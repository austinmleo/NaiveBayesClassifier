def test(data, classifier, allClasses, wordTotals, classTotals, grandTotal):
    bestClass = allClasses[0]
    bestProb = 0

    for c in allClasses:
        classTotal = classTotals[c]

        for word in data:
            if len(word) < 6:
                continue
            try:
                wordTotal = wordTotals[word]
            except KeyError as e:
                continue

            prob = classifier[word][c]*(1./wordTotal)*(float(classTotal)/grandTotal)

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

def test(data, classifier, allClasses, wordTotals, classTotals, grandTotal):
    bestClass = allClasses[0]
    bestProb = 0

    probabilities = {}

    for c in allClasses:
        classTotal = classTotals[c]

        prob = 1.

        for word in data:
            try:
                wordTotal = wordTotals[word]
            except KeyError as e:
                continue

            prob *= classifier[word][c]*(1./wordTotal)*(float(classTotal)/grandTotal)

            if prob > bestProb:
                bestProb = prob
                bestClass = c

        probabilities[c] = prob

    ranked = sorted(probabilities.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    bestClass = ranked[0][0]
    bestProb = ranked[0][0]

    return bestClass, bestProb


def getClassTotal(c, classifier):
    total = 0
    for word in classifier.keys():
#        print "Word: {}".format(word)
#        print "Class: {}".format(c)
#        print "Classifier: {}".format(classifier[word])
        total += classifier[word][c]

    return total

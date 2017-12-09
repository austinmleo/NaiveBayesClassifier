def test(data, classifier, classes, allClasses, wordTotals, classTotals, grandTotal):

    probabilities = {}

    for c in allClasses:
        classTotal = classTotals[c]

        prob = 1. if data else 0.


        for word in data:
            if len(word) < 11:
                continue
            try:
                wordTotal = wordTotals[word]
            except KeyError as e:
                continue

            prob *= classifier[word][c]*(1./wordTotal)*(float(classTotal)/grandTotal)

        probabilities[c] = prob

    ranked = sorted(probabilities.iteritems(), key=lambda (k,v): (v,k), reverse=True)



    return ranked[0:classes]


def getClassTotal(c, classifier):
    total = 0
    for word in classifier.keys():
#        print "Word: {}".format(word)
#        print "Class: {}".format(c)
#        print "Classifier: {}".format(classifier[word])
        total += classifier[word][c]

    return total

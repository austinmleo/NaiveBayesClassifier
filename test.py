def test(data, classifier):
    allClasses = list(classifier.keys())
    bestClass = allClasses[0]
    bestProb = 0

    wordTotals = {}
    for word in classifier:
        wordTotals[word] = sum(classifier[word].values())

    grandTotal = sum(wordTotal.values())

    for c in allClasses:
        classTotal = getClassTotal(c, classifier)

        for word in data:
            wordTotal = wordTotal[word]

            prob = classifier[word[c]]*(1/wordTotal)*(classTotal/grandTotal)

            if prob > bestProb:
                bestProb = prob
                bestClass = c




def getClassTotal(c, classifier):
    total = 0
    for word in classifier:
        total += classifier[word[c]]

    return total

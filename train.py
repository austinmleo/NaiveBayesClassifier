def train(data, classifier, classification, allClasses):

    for word in data:
        try:
            row = classifier[word]
        except KeyError:
            row = {}
            for c in allClasses:
                row[c] = 0
        row[classification] += data[word]
        classifier[word] = row



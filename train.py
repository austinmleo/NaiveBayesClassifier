def train(data, classifier, classifications, allClasses):
    for word in data:
        try:
            row = classifier[word]
        except (KeyError, TypeError) as e:
            row = {}
            for c in allClasses:
                row[c] = 0
        for c in classifications:
            row[c] += data[word]
        classifier[word] = row

    return classifier

import sys
import os

def getFilenames(path):
    files = []

    for r, d, f in os.walk(path):
        for name in f:
            files.append(os.path.join(r, name))

    return files

def main():
    
    files = getFilenames('./20_newsgroups/')

    print files
    print len(files)

    allClasses = list(files.keys())
    classifier = {}
    for classification in files:
        breakCount = 0
        for f in files[classification]:
            wordCounts = getWordCount(f)
            classifier = train(wordCount, classifier, classification, allClasses)

            breakCount += 1
            if breakCount > 800:
                break




    exit()


if __name__ == '__main__':
    main()



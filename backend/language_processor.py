from nltk.corpus import wordnet as wn


def getHelpWords(word):
    fullWords = []
    # Each synset represents a different concept:
    for ss in wn.synsets(word):
        fullWords.append(ss.lemma_names())
    finalWordList = [item for sublist in fullWords for item in sublist]
    return finalWordList


def getDefiningWords(word):
    fullWords = []
    # Each synset represents a different concept
    for ss in wn.synsets(word):
        fullWords.append(ss.definition())
    return fullWords

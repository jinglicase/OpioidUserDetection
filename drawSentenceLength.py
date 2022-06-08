import os
from numpy import array, asarray
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import matplotlib.pyplot as plt

# Get the distribution of the length of posts before the data preprocessing.
# def beforePreprocess(df, maxNum):
#     X = df.iloc[:, 5]
#     X = X.values.tolist()
#     numWordList = []
#     for i in range(maxNum + 1):
#         numWordList.append(0)
#
#     maxLength = 0
#     totalLength = 00
#     for i in range(len(X)):
#         tempList = X[i].split(' ')
#         sentenceLength = len(tempList)
#
#         if maxLength < sentenceLength:
#             maxLength = sentenceLength
#
#         totalLength += sentenceLength
#         index = int(sentenceLength / 10)
#         if (index < maxNum):
#             numWordList[index] += 1
#         else:
#             numWordList[-1] += 1
#     averageLength = totalLength / len(X)
#     return numWordList, averageLength

# Get the distribution of the length of posts after the data preprocessing.
def afterPreprocess(df, maxNum):
    stop = stopwords.words('english')
    X = df.iloc[:, 5].apply(lambda x: [item for item in x.split() if item not in stop])

    lemma = WordNetLemmatizer()
    X = X.apply(lambda x: [lemma.lemmatize(item) for item in x])

    X = X.values.tolist()
    numWordList = []
    for i in range(maxNum + 1):
        numWordList.append(0)

    maxLength = 0
    totalLength = 0
    for i in range(len(X)):
        sentenceLength = len(X[i])

        if maxLength < sentenceLength:
            maxLength = sentenceLength

        totalLength += sentenceLength
        index = int(sentenceLength / 10)
        if (index < maxNum):
            numWordList[index] += 1
        else:
            numWordList[-1] += 1
    averageLength = totalLength / len(X)
    return numWordList, averageLength

def drawBar(numWordList):
    requireLength = 31
    numWordList = numWordList[0:requireLength]
    y_pos = np.arange(0, len(numWordList*10), 10)
    for i in range(len(numWordList)):
        plt.bar(y_pos, numWordList, width=10)

    plt.xticks([0, 40, 90, 140, 190, 240, 290, 300], [10, 50, 100, 150, 200, 250, 300, '300+'], rotation=60)

    plt.xlabel('The length of each post', fontsize=15)
    plt.ylabel('The number of posts', fontsize=15)

    plt.show()

def main():
    scriptDir = os.path.dirname(__file__)
    inputFile = os.path.join(scriptDir, "../dataCollection/dataset1000/bidataOpiumStreet1020.csv")

    df = pd.read_csv(inputFile, delimiter=',', encoding='latin-1')
    maxNum = 30

    after_numWordList, after_averageLength = afterPreprocess(df, maxNum)
    drawBar(after_numWordList)

if __name__ == '__main__':
    main()
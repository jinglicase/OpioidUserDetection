import os
from numpy import array, asarray
import pandas as pd
import numpy as np
from SlangList import SlangList

def numKeyStreet(df, drugList, drugStreetList):
    X = df.iloc[:, 4]
    X = X.apply(
        lambda x: [item for item in x.split('^')])  # <class 'pandas.core.series.Series'> # e.g. [chocolate, opiates]
    X = X.tolist()
    print(type(X))
    print(X)

    combNum = 0
    keyNum = 0
    streetNum = 0

    for i in range(len(X)):
        keyFlag = False
        streetFlag = False
        for j in range(len(X[i])):
            if (X[i][j] in drugList):
                keyFlag = True
            if (X[i][j] in drugStreetList):
                streetFlag = True
        if keyFlag == True and streetFlag == True:
            combNum += 1
        elif keyFlag == True and streetFlag != True:
            keyNum += 1
        elif keyFlag != True and streetFlag == True:
            streetNum += 1
    print("combNum = " + str(combNum))
    print("keyNum = " + str(keyNum))
    print("streetNum = " + str(streetNum))

def makeDict(df, drugList, drugStreetList):
    dict = {}
    X = df.iloc[:, 5]
    X = X.apply(lambda x: [item for item in x.split()])  # <class 'pandas.core.series.Series'> # e.g. [chocolate, opiates]
    X = X.tolist()
    for i in range(len(X)):
        for j in range(len(X[i])):
            if X[i][j] not in drugList and X[i][j] not in drugStreetList:
                continue
            else:
                if X[i][j] in dict:
                    dict[X[i][j]] += 1
                else:
                    dict[X[i][j]] = 1
    sortedDict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    print(sortedDict)

def main():
    scriptDir = os.path.dirname(__file__)
    inputFile = os.path.join(scriptDir, "dataCollection/dataset1000/bidataOpiumStreet1020.csv")

    df = pd.read_csv(inputFile, delimiter=',', encoding='latin-1')

    drugType = 'opium'
    sl = SlangList(drugType)
    drugList = sl.getDrugList(drugType)
    drugStreetList = sl.getDrugStreetList(drugType)

    numKeyStreet(df, drugList, drugStreetList)

    makeDict(df, drugList, drugStreetList)


if __name__ == '__main__':
    main()
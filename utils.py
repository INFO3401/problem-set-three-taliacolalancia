import pandas as pd
import matplotlib.pyplot as plt

def helloWorld():
    print("Hello World")

def loadAndCleanData(filename):
    data = pd.read_csv(filename)
    data.fillna(0)
    print(data)
    return data

def computePDF(target, data):
    data[target].plot.kde()
    plt.show()

def viewDistribution(target, data):
    data[target].hist()
    plt.show()

def viewLogDistribution(viewDistribution, data):
    data[viewDistribution].hist()
    plt.show()

def computeDefaultRisk(filename, bin, target, data):
    count = 0.0
    for i,data in data.iterrows():
        if data[target] >= bin[0] and data[target] < bin[1]:
            count += 1

    totalData = len(data)

    probability = count / totalData

    return probability

def predictDefaultRisk():


 def computerProbability(feature, bin, data):
    count = 0.0
    for i,datapoint in data.iterrows():
        if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            count += 1

    totalData = len(data)

    probability = count / totalData

    return probability

class Poll:
    # Start with a poll name and data
    def __init__(self, name, df):
        self.outlet = name
        self.data = df.loc[df['Poll'] == name]

    def getMostRecentPoll(self):
        return self.data.iloc[0]

    def countPoll(self):
        return len(self.data)

    def changeInPoll(self, candidate):
        candidateData = self.data[candidate]
        return candidateData.iloc[0] - candidateData.iloc[len(candidateData) - 1]

    def avgInPoll(self, candidate):
        return self.data[candidate].mean()

    def medianInPoll(self, candidate):
        return self.data[candidate].median()

    def correlatedPolls(self, candidate1, candidate2):
        if (self.countPoll() == 1):
            print("Not enough data")
            return 0
        else:
            return self.data[canidate1].corr(self.data[candidate2])

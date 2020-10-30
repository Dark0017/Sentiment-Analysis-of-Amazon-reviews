import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle
from dataCleaning import getTrainingData

#Classifier Training____________________________________________________________________________________________________
def trimDataset(df, training_size = 0):
    if(training_size > 0):
        df = df.sample(n = training_size)
        return df

def makeClassifierPickle(training_size = 0):
    import os
    source = os.path.dirname(__file__)
    fileName = os.path.join(source, 'CleanDB.csv')
    if not os.path.isfile(fileName):
        getTrainingData()
    selfSource = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(selfSource, 'CleanDB.csv'))
    if(training_size > 0):
        df = trimDataset(df, training_size)
    # reviews are features and the sentiment polarity is the label.
    X, y = df.loc[:, 'review'], df.loc[:, 'type']

    # split the data into train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    countVect = CountVectorizer()
    tfidfTransformer = TfidfTransformer()
    classifier = LogisticRegression(random_state=1, max_iter=500)
    sentimentPipeline = Pipeline([('vect', countVect), ('tfidf', tfidfTransformer), ('clf', classifier)])

    #fit data into model.
    sentimentPipeline.fit(X_train.apply(lambda x: np.str_(x)), y_train)
    #store trained model.
    import os; from pathlib import Path
    source = os.path.dirname(Path(__file__).parent)
    fileName = os.path.join(source, 'Driver Code', 'trainedClassifier.clf')
    with open(fileName, 'wb') as clfFile:
        pickle.dump(sentimentPipeline, clfFile)
    y_predicted =  sentimentPipeline.predict(X_test.apply(lambda x: np.str_(x)))
    avgAccuracy = np.mean(y_predicted  == y_test)
    print("Classifier with average testing accuracy of {} exported to 'root/Driver Code' as pickle file.".format(avgAccuracy))
    return

if __name__ == '__main__':
    makeClassifierPickle()
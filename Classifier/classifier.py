import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv('CleanDB.csv')
df = df.sample(n = 60000)

#reviews are features and the sentiment polarity is the label.
X, y = df.loc[:, 'review'], df.loc[:, 'type']

#split the data into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y)

'''
#Tokenizing the data to obtain feature vectors.


#return a dictionary of the form {index of word : frequency of word} in the whole review corpus. In our case, shape = (1088873, 172690)
#we have to convert each str object in the array to str_ in order for count vectroizer and the tfID vectorizer to iterate over them.
X_train_counts = countVect.fit_transform(X_train.apply(lambda x: np.str_(x)))

#fit the calculate word frequencies according to their distribution over the corupsu. i.e. values less meaningful will now have less frequency and vice-versa.

X_train_tfidf = tfidfTransformer.fit_transform(X_train_counts)w

#Dummy classifier code (default parameters)

'''
countVect = CountVectorizer()
tfidfTransformer = TfidfTransformer()
classifier = LogisticRegression(random_state=1, max_iter=500)
sentimentPipeline = Pipeline([('vect', countVect), ('tfidf', tfidfTransformer), ('clf', classifier)])

sentimentPipeline.fit(X_train.apply(lambda x: np.str_(x)), y_train)

file = open('trainedClassifier.clf', 'wb')
pickle.dump(sentimentPipeline, file)
file = open('trainedClassifier.clf', 'rb')
loaded_clf = pickle.load(file)

y_predicted = loaded_clf.predict(X_test.apply(lambda x: np.str_(x)))
avgAccuracy = np.mean(y_predicted == y_test)

testReview = {"This is not the actual Optimum Nutrition product. It's fake. Optimum Nutrition website lists few guidelines to confirm that the box is original. This box does not match most of the descriptions there. Firstly the box contains typos at a lot of places, it does not have batch number and manufacturing details. Amazon should not allow fake products to be sold on their website"}

testPrediction = sentimentPipeline.predict(testReview)


def getPrediction(reviewText):
    prediction = sentimentPipeline.predict(testReview)
    return int(testPrediction[0])


print(getPrediction(testReview))

print(avgAccuracy)

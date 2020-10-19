import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv('CleanDB.csv')

#reviews are features and the sentiment polarity is the label.
X, y = df.loc[:, 'review'], df.loc[:, 'type']

#split the data into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)

'''
#Tokenizing the data to obtain feature vectors.


#return a dictionary of the form {index of word : frequency of word} in the whole review corpus. In our case, shape = (1088873, 172690)
#we have to convert each str object in the array to str_ in order for count vectroizer and the tfID vectorizer to iterate over them.
X_train_counts = count_vect.fit_transform(X_train.apply(lambda x: np.str_(x)))

#fit the calculate word frequencies according to their distribution over the corupsu. i.e. values less meaningful will now have less frequency and vice-versa.

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#Dummy classifier code (default parameters)

'''
count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()
classifier = LogisticRegression()
sentiment_pipeline = Pipeline([('vect', count_vect), ('tfidf', tfidf_transformer), ('clf', classifier)])

sentiment_pipeline.fit(X_train.apply(lambda x: np.str_(x)), y_train)

y_predicted = sentiment_pipeline.predict(X_test.apply(lambda x: np.str_(x)))
avg_accuracy = np.mean(y_predicted == y_test)

print(avg_accuracy)














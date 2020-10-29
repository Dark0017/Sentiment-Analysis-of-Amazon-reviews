import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from bs4 import BeautifulSoup
import requests
import csv

#scraper______________________________________________________________________________

def getReviews(productURL):
    user_link = productURL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    source = requests.get(user_link, headers=headers).text

    soup = BeautifulSoup(source, 'lxml')
    print(soup.prettify())

    names = []
    review = []

    # loop

    for i in soup.find_all('span', class_='a-profile-name'):
        string = i.text
        names.append(string.strip())

    for i in soup.find_all('div',
                           class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content'):
        string = i.text
        review.append(string.strip())

    # storage

    file_name = 'reviews.csv'

    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Sr.No', 'Name', 'Review'])

        for i in range(len(names)):
            writer.writerow([i, names[i], review[i]])





#classifier______________________________________________________________________________

df = pd.read_csv('CleanDB.csv')
df = df.sample(n = 60000)

#reviews are features and the sentiment polarity is the label.
X, y = df.loc[:, 'review'], df.loc[:, 'type']

#split the data into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y)

countVect = CountVectorizer()
tfidfTransformer = TfidfTransformer()
classifier = LogisticRegression(random_state=1, max_iter=500)
sentimentPipeline = Pipeline([('vect', countVect), ('tfidf', tfidfTransformer), ('clf', classifier)])

sentimentPipeline.fit(X_train.apply(lambda x: np.str_(x)), y_train)

y_predicted = sentimentPipeline.predict(X_test.apply(lambda x: np.str_(x)))
avgAccuracy = np.mean(y_predicted == y_test)



def getPrediction(reviewText):
    prediction = sentimentPipeline.predict(reviewText)
    return int(prediction[0])




#Driver Code:
getReviews(input('Enter amazon product URL: '))

userReviews = pd.read_csv('reviews.csv')

userReviews["Prediction"] = [getPrediction(i) for i in userReviews.loc[:, 'Review']]

print(userReviews.head(3))


import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import pickle
from classifier import makeClassifierPickle

#scraper______________________________________________________________________________
def getAndStoreReviews(productURL):
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

def getClassifierFile():
    import os; from pathlib import Path
    source = os.path.dirname(Path(__file__))
    fileName = os.path.join(source, 'trainedClassifier.clf')
    if( not os.path.isfile(fileName)):
        makeClassifierPickle()
    with open('trainedClassifier.clf', 'rb') as clfFile:
        classifier = pickle.load(clfFile)
        return classifier

#Driver Code:
if __name__ == '__main__':
    getAndStoreReviews((input('Enter amazon product URL: ')))
    userReviews = pd.read_csv('reviews.csv')
    classifier = getClassifierFile()
    userPredictions = classifier.predict(userReviews['Review'].apply(lambda x: np.str_(x)))
    userReviews["Predictions"] = userPredictions
    print(userReviews)
classifier.py uses the cleanDB.csv file obtained from the cleaning script.

It does the following:
1.'count_vec' Creates a count vectorizer that returns a dictionary {word's index in doc: it's frequency} in the form of a sparse matrix using scikit learn's scipy implementation.
 
2.'tfidf_transformer' Applies the Total frequency times inverse document frequency(tfidf) technique, which basically means the words' total frequency throughout the review set is divided by their per review frequency, distributing the overall values (nearly) evenly.

3.'classifier' is the classifier object. Rpleace its value to that of choice to test different classifiers.

4.Necessary preprocessing when dealing with vectorizers: For any X_train.csv that we wish to use as our training set, always pass X_train.apply(lamba x: np.str_(x)) as the training dataframe to the classifier. Also, when predicting values, do the same with the test or prediction set, replacing "X_train" with the name of the specific test or prediction set.
Visit https://stackoverflow.com/questions/39303912/tfidfvectorizer-in-scikit-learn-valueerror-np-nan-is-an-invalid-document for more details.

5.'sentiment_pipeline' involves step 1-3 in that order, preprocesses the training data and trains the classifier of choice.



HyperParameter Tuning remains to be done.

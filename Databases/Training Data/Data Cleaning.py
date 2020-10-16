import pandas as pd

pd.set_option('display.max_columns', 20)

#put the path to directories to these csv files inside these quotes, I had them in same folder as my data cleaning file
cellPhoneDB = pd.read_csv("AmazonCellphoneReviews.csv")
fineFoodDB = pd.read_csv('AmazonFineFoodReviews.csv')
amazonProductDB = pd.read_csv('AmazonProductReviews.csv')
unlockedMobileDB = pd.read_csv('AmazonUnlockedMobileReviews.csv')
musicInstrumentDB = pd.read_csv('MusicalInstrumentReviews.csv')

#function to classify rating as positive negative or neutral
def reviewClass(rating):
    if rating == 3:
        return 0
    elif rating > 3:
        return 1
    elif rating < 3:
        return -1


#cellPhoneDataset

#if review is positive then 1, negative then -1, neutral then 0
reviewType = [ reviewClass(i) for i in cellPhoneDB.loc[:, 'rating'].values]

cleanDF = pd.DataFrame({'Product': cellPhoneDB.loc[:,'asin'], 'review': cellPhoneDB.loc[:,'body'], 'rating': cellPhoneDB.loc[:,'rating'], 'type': reviewType})

#AmazonFineFoodsDataset
reviewType = [ reviewClass(i) for i in fineFoodDB.loc[:, 'Score'].values]
tempDF = pd.DataFrame({'Product': fineFoodDB.loc[:,'ProductId'], 'review': fineFoodDB.loc[:,'Text'], 'rating': fineFoodDB.loc[:,'Score'], 'type': reviewType})

cleanDF = cleanDF.append(tempDF, ignore_index= True)

#AmazonProductsDataset
reviewType = [ reviewClass(i) for i in amazonProductDB.loc[:, 'reviews.rating'].values ]
tempDF = pd.DataFrame({'Product': amazonProductDB.loc[:,'asins'], 'review': amazonProductDB.loc[:,'reviews.text'], 'rating': amazonProductDB.loc[:,'reviews.rating'], 'type': reviewType})

cleanDF = cleanDF.append(tempDF, ignore_index= True)

#UnlockedPhonesDataset
reviewType = [ reviewClass(i) for i in unlockedMobileDB.loc[:, 'Rating'].values ]
tempDF =  pd.DataFrame({'Product': unlockedMobileDB.loc[:,'Product Name'], 'review': unlockedMobileDB.loc[:,'Reviews'], 'rating': unlockedMobileDB.loc[:,'Rating'], 'type': reviewType})

cleanDF = cleanDF.append(tempDF, ignore_index= True)

#MusicInstrumentDataset
reviewType = [ reviewClass(i) for i in musicInstrumentDB.loc[:, 'overall'].values ]
tempDF = pd.DataFrame({'Product': musicInstrumentDB.loc[:,'asin'], 'review': musicInstrumentDB.loc[:,'reviewText'], 'rating': musicInstrumentDB.loc[:,'overall'], 'type': reviewType})

cleanDF = cleanDF.append(tempDF, ignore_index= True)


cleanDF[['Product', 'review', 'rating', 'type']].to_csv("CleanDB.csv", index = False)
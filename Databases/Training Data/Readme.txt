-This data cleaning script will extract the following collumns from the 5 datasets listed at the 
 end of this file:

1. Product: It is the product name or id
2. review : The actual text review for the product
3. rating : Star rating given by the customer 
4. type   : The type of review based on the star rating:
		1 : positive : > 3 stars
		0 : neutral  : = 3 stars
	       -1 : negative : < 3 stars

-The final file will have 1088872 Entries.

-The entries aren't checked for any outliers/NaN values.

https://data.world/datafiniti/consumer-reviews-of-amazon-products
AmazonProductReviews.csv

https://www.kaggle.com/snap/amazon-fine-food-reviews
AmazonFineFoodReviews.csv

https://www.kaggle.com/eswarchandt/amazon-music-reviews?select=Musical_instruments_reviews.csv
MusicalInstrumentReviews.csv

https://www.kaggle.com/grikomsn/amazon-cell-phones-reviews?select=20191226-reviews.csv
AmazonCellphoneReviews.csv

https://www.kaggle.com/PromptCloudHQ/amazon-reviews-unlocked-mobile-phones
AmazonUnlockedMobileReviews.csv


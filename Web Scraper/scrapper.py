from bs4 import BeautifulSoup
import requests
import csv

sourceURL = 'https://www.amazon.in/Samsung-Fully-Automatic-WA62M4100HY-TL-Imperial/dp/B0747XV38N/ref=sr_1_3?dchild=1&pf_rd_p=9d2096f8-d1f7-4799-accb-686424bc6fa3&pf_rd_r=1W2C75V9J6GSCG7AN5ZK&qid=1602518835&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-3'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
source = requests.get(sourceURL, headers = headers).text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

names = []
review = []

#loop

for i in soup.find_all('span', class_ ='a-profile-name'):
    string = i.text
    names.append(string.strip())

for i in soup.find_all('div', class_ ='a-expander-content reviewText review-text-content a-expander-partial-collapse-content'):
    string = i.text
    review.append(string.strip())

#storage

file_name = 'reviews.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Name', 'Review'])

    for i in range(len(names)):
        writer.writerow([i, names[i], review[i]])

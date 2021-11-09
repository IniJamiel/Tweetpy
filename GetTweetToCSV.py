
#Do pip install for the following libraries: -tweepy

import tweepy
import csv

import datetime

#This Code will crawl data from the twitter API to get number of tweets of certain keywords, in a configured interval

#After collecting it into a list, it will pass it to a CSV file named "table.csv"


#Change with your twitter API keys
label ='' #fill it with your label

user_token = ''

user_secret_token = ''

bearer = ''

access_token = ''

access_token_secret = ''

auth = tweepy.OAuthHandler(user_token, user_secret_token)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.wait_on_rate_limit = True
client = tweepy.Client(auth)

auth.set_access_token(access_token, access_token_secret)

counter = 0
number_of_tweets = 2000


#Change to desired range
year = 2021

begin_year = datetime.date(year, 11, 1)
end_year = datetime.date(year, 11, 8)

#Change to 1 for daily tweets or 7 for weekly counts ("Limited to 100 tweets as per Twitter basic API)
interval = 1

one_day = datetime.timedelta(days=interval)

next_day = begin_year

keyword = input("Insert keyword : ")
header = ['date', 'number of tweets']
data = []
total = 0
for day in range(0, 366):
    if next_day > end_year:
        break

    month = next_day.month
    if month < 10:
        monthh = '0' + str(month)
    else:
        monthh = str(month)

    date = next_day.day
    if date < 10:
        datee = '0' + str(date)
    else:
        datee = str(date)

    counter = 0
    for tweet in api.search_30_day(label, keyword, fromDate='' + str(year) + monthh + datee + '00' + '00',
                                   toDate='' + str(year) + monthh + datee + '23' + '59'):
        counter += 1
    total += counter
    data.append([next_day, counter])
    next_day += one_day

with open('table.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

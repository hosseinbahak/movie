"""
if you want just a small part of dataset you can run this file
this file print some lines of movies_metadata.csv
so you have to save these line in a new file and load your database with new csv files
first you need to run this file for movies and then the ./import_credits.py file
this file print 300 last movies or movies from Iran
you can change this file if you like to print your desired output
"""
from csv import DictReader
from datetime import datetime

# all the dates in movies_metadata.csv
dates = []
for row in DictReader(open('./movies_metadata.csv')):
    try:
        dates.append(datetime.strptime(str(row['release_date']), '%Y-%m-%d'))
    except:
        pass

# vote counts
votes = []
for row in DictReader(open('./movies_metadata.csv')):
    try:
        votes.append(int(row['vote_count']))
    except:
        pass

votes = sorted(votes)
dates = sorted(dates)
# print(votes[-300], votes[-1])
# print(dates[-10000], dates[-1])

# number of lines that we want to add to our test dataset
l = [0]
c = 0
for row in DictReader(open('./movies_metadata.csv')):
    c += 1
    try:
        # 300 last movies and if it is from iran
        if (dates[-10000] <= datetime.strptime(str(row['release_date']), '%Y-%m-%d') and votes[-300] <= int(row['vote_count'])) or "Iran" in str(row['production_countries']):
            l.append(c)
    except:
        pass

# print(len(l))
# print lines so that we use it in our test dataset
i = 0
c = 0
for line in open('./movies_metadata.csv', 'r'):
    if len(l) <= c:
        break
    if i == l[c]:
        print(line, end='')
        c+=1
    i+=1

"""
* if you don't know what this file is you should look at ./import_movies.py

this file grabs the movie ids from ./movies_metadata.csv file 
and then print the related credits lines in ./credits.csv file
if you want small part of dataset you should first run ./import_movies.py file and then this file.
"""
from csv import DictReader

# list of ids in movies_metadata 
list_of_ids = []
for row in DictReader(open('./movies_metadata.csv')):
    list_of_ids.append(row['id'])

# number of lines that we want to add to our test dataset in credits
lis = [0]
c = 0
for row in DictReader(open('./credits.csv')):
    c += 1
    if row['id'] in list_of_ids:
        list_of_ids.remove(row['id'])
        lis.append(c)

# print lines so that we use it in our test dataset
i = 0
c = 0
for line in open('./credits.csv', 'r'):
    if len(lis) <= c:
        break
    if i == lis[c]:
        print(line, end='')
        c+=1
    i+=1

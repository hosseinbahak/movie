"""
if you want just a small part of dataset you can run this file
this file print some lines of movies_metadata.csv
so you have to save these line in a new file and load your database with new csv files
first you need to run this file for movies and then the ./import_credits.py file
this file print 300 last movies or movies from Iran
you can change this file if you like to print your desired output
you can run `python ./import_movies.py > movies_metadata_new.csv` and then change 
the new file with the original file
"""
import csv
from datetime import datetime
from io import StringIO

# all the dates in movies_metadata.csv
dates = []
for row in csv.DictReader(open('./movies_metadata.csv')):
    try:
        dates.append(datetime.strptime(str(row['release_date']), '%Y-%m-%d'))
    except:
        pass

# vote counts
votes = []
for row in csv.DictReader(open('./movies_metadata.csv')):
    try:
        votes.append(int(row['vote_count']))
    except:
        pass

votes = sorted(votes)
dates = sorted(dates)
# print(votes[-300], votes[-1])
# print(dates[-10000], dates[-1])

# number of lines that we want to add to our test dataset
output = StringIO(newline='\n')
field_names = "adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count".split(',')
with open('./movies_metadata.csv', 'r', newline='\n') as f:
    writer = csv.DictWriter(output, fieldnames=field_names)
    reader = csv.DictReader(f)
    writer.writeheader()
    for row in reader:
        try:
            # 200 last movies and if it is from iran
            if (dates[-10000] <= datetime.strptime(str(row['release_date']), '%Y-%m-%d') and votes[-200] <= int(row['vote_count'])) or "Iran" in str(row['production_countries']):
                writer.writerow(row)
        except:
            pass

data = [line.strip() for line in output.getvalue().splitlines()]
for line in data:
    print(line)
# print(len(data))
"""
* if you don't know what this file is you should look at ./import_movies.py

this file grabs the movie ids from ./movies_metadata.csv file 
and then print the related credits lines in ./credits.csv file
if you want small part of dataset you should first run ./import_movies.py file and then this file.
first make sure that "./movies_metadata_new.csv" file you create with "import_movies.py" is renamed to "movies_metadata.csv"
so you can run `python ./import_credits.py > credits_new.csv` and then change 
the new file with the original file 
"""
import csv
from io import StringIO

# list of ids in movies_metadata 
list_of_ids = []
for row in csv.DictReader(open('./movies_metadata.csv')):
    list_of_ids.append(row['id'])

# number of lines that we want to add to our test dataset in credits
output = StringIO(newline='\n')
field_names = "cast,crew,id".split(',')
with open('./credits.csv', 'r', newline='\n') as f:
    writer = csv.DictWriter(output, fieldnames=field_names)
    reader = csv.DictReader(f)
    writer.writeheader()
    for row in reader:
        try:
            if row['id'] in list_of_ids:
                list_of_ids.remove(row['id'])
                writer.writerow(row)
        except:
            pass

data = [line.strip() for line in output.getvalue().splitlines()]
for line in data:
    print(line)
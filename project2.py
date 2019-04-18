#import csv module
import csv 

d = dict()
# reading csv file
with open ('2016_movie_data.csv', 'rt', encoding = 'ISO-8859-1') as csvfile:

    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    for row in csvreader:
        for key, value in row.items():
            if d.get(key) is None:
                d[key] = [value]
            else:
                d[key].append(value)
   
print(d)
print('keys:', d.keys())

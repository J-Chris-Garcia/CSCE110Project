import csv 
from datetime import datetime

moviespermonth = {} #use this for question 2
date_format = '%m/%d/%Y'

with open ('2016_movie_data.csv', 'rt', encoding = 'ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #skips first line
    
    for row in csvreader:
        datetime_obj = datetime.strptime(row[1], date_format) #line 12/13 get the month from the date
        month = datetime_obj.strftime("%B")
        
        if month in moviespermonth.keys():
            moviespermonth[month] += 1
        else:
            moviespermonth[month] = 1

        
totalmovies = sum(moviespermonth.values())
print(f"The total number of movies released: {totalmovies}")    
print(moviespermonth)

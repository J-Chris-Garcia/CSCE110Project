#File: project2.py
#Author: Josue Garcia, Elissa Grosz, and CheungHing Lam
#Date: 05/01/2019
#Email: chrisg000@tamu.edu, elissagrosz@tamu.edu, Cheunghing1113@tamu.edu
#Description: Option 2: The Netflix Movie Tracker, This code goes through a CSV file with netflix movie data and outputs related stats
import csv
from datetime import datetime

movies_per_month = {} #use this for question 2
genre_per_month = {} #use this for question 5
ratings = []
tickets_per_dist = {} #use this for question 4
tickets_per_month = {} #use this for question 3

date_format = '%m/%d/%Y' #used to convert data string to datetime object
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #used to add months not in csv

with open ('2016_movie_data.csv', 'rt', encoding = 'ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        datetime_obj = datetime.strptime(row[1], date_format) #line 12/13 get the month from the date
        month = datetime_obj.strftime("%B")
        
        if month in tickets_per_month: #this gets us tickets per month
            tickets_per_month[month] += int(row[5].replace(',',''))
        else:
            tickets_per_month[month] = int(row[5].replace(',',''))

        if row[2] in tickets_per_dist: #these give us the tickets per dist
            tickets_per_dist[row[2]] += int(row[5].replace(',',''))
        else:
            tickets_per_dist[row[2]] = int(row[5].replace(',',''))

        if month in movies_per_month.keys(): #these give us movies per month
            movies_per_month[month] += 1
        else:
            movies_per_month[month] = 1

        if row[3] in genre_per_month and month in genre_per_month[row[3]]: #these give us genre per month
            genre_per_month[row[3]][month] += 1
        elif row[3] in genre_per_month:
            genre_per_month[row[3]][month] = 1
        else:
            genre_per_month[row[3]] = {month:1}

        if row[4] in ratings: #this gets the different distinct ratings
            continue
        else:
            ratings.append(row[4])

for genre, mon in genre_per_month.items(): #this adds entries to genre_per_month; when there is a month with no release for this genre it adds a nested dictionary of month:0
    for month in months:
        if month in mon:
            continue
        else:
            genre_per_month[genre][month] = 0
        
totalmovies = sum(movies_per_month.values())
totaltickets = sum(tickets_per_month.values())
maxmovie, moviemonth = max(zip(movies_per_month.values(), movies_per_month.keys())) #this finds the max amount of movies per month
maxtickets, ticketmonth = max(zip(tickets_per_month.values(), tickets_per_month.keys())) #this finds the max amount of tickets per month

print("========Dataset details========\n")
print(f"Number of Movies: {totalmovies}")
print(f"Number of different genres: {len(genre_per_month)}")
print(f"Number of different MPAA: {len(ratings)}")
print(f"Number of different distributors: {len(tickets_per_dist)}")
print(f"Total number of tickets sold: {totaltickets}")
print("\n================================\n")
print(f"Most number of movies released ({maxmovie}) in {moviemonth}.")
print(f"Most amount of tickets sold ({maxtickets}) in {ticketmonth}.")
print("\n================================\n")
print("========Tickets sold by distributors========\n")

Others = 0 #this will get the dictionary with others category
for dist, amount in tickets_per_dist.items():
    tickets_per_dist[dist] = (amount/totaltickets)*100
    
for dist in list(tickets_per_dist):
    if tickets_per_dist[dist] < 1:
        Others += tickets_per_dist[dist]
        del tickets_per_dist[dist]
tickets_per_dist["Others"] = Others

tickets_per_dist = dict(sorted(tickets_per_dist.items(), key=lambda x: x[1], reverse=True))

for dist,amount in tickets_per_dist.items():
    print(f"{dist}  :  {round(amount, 2)}%")
    
print("\n================================")

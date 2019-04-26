#File: project2.py
#Author: Josue Garcia, Elissa Grosz, and CheungHing Lam
#Date: 05/01/2019
#Email: chrisg000@tamu.edu, elissagrosz@tamu.edu, Cheunghing1113@tamu.edu
#Description: Option 2: The Netflix Movie Tracker. This code goes through a CSV file with netflix movie data and outputs related statistics.

#import modules
import csv
from datetime import datetime

movies_per_month = {} #use this for question 2
genre_per_month = {} #use this for question 5
ratings = []
tickets_per_dist = {} #use this for question 4
tickets_per_month = {} #use this for question 3

date_format = '%m/%d/%Y' #used to convert data string to datetime object
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #used to add months not in csv

file_name = input("Enter the name of the csv file (include .csv): ")
#create csv file
with open (file_name, 'rt', encoding = 'ISO-8859-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #skip headers
    
    #go through each row to extract data
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
        
totalmovies = sum(movies_per_month.values()) #finds the total number of movies released in 2016
totaltickets = sum(tickets_per_month.values()) #finds total number of tickets sold in 2016
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
lab=[]
for i in tickets_per_dist:
    lab.append(i)
num=[]
for i in tickets_per_dist.values():
    num.append(i)


#import matplotlib module
import matplotlib.pyplot as plot

#create a plot for question 2
plot.figure(1)
#plotting bar graph of number of movies released each month
plot.bar(months, [movies_per_month["January"], movies_per_month["February"], movies_per_month["March"], movies_per_month["April"], movies_per_month["May"],  movies_per_month["June"], movies_per_month["July"], movies_per_month["August"], movies_per_month["September"], movies_per_month["October"], movies_per_month["November"], movies_per_month["December"]], color='b', linestyle='-')
#labeling graph for question 2
plot.ylabel(' Number of Movies')
plot.xlabel('Month')
plot.title('Number of movies released in different months of 2016')
plot.savefig("question2-plot.pdf")
plot.show()

#create a plot for question 3
plot.figure(2)
#plotting line graph of number of tickets sold each month
plot.plot(months, [tickets_per_month["January"], tickets_per_month["February"], tickets_per_month["March"], tickets_per_month["April"], tickets_per_month["May"],  tickets_per_month["June"], tickets_per_month["July"], tickets_per_month["August"], tickets_per_month["September"], tickets_per_month["October"], tickets_per_month["November"], tickets_per_month["December"]], color='b', linestyle='-')
#labeling graph for question 3
plot.ylabel('Number of tickets sold (in millions)')
plot.xlabel('Month')
plot.title('Number of tickets sold in different months of 2016')
plot.savefig("question3-plot.pdf")
plot.show()

#create plot for question 4
plot.figure(3)
#plotting the percentage of tickets sold by each distributor
plot.pie(num, labels=lab, shadow=True, autopct='%1.1f%%')
plot.axis('equal')
plot.title("Percentage of tickets sold by different distributors")
plot.show()

#create plot for question 5
plot.figure(4)
#plotting the number of movies from drama released each month
plot.plot(months, [genre_per_month["Drama"]["January"], genre_per_month["Drama"]["February"], genre_per_month["Drama"]["March"], genre_per_month["Drama"]["April"], genre_per_month["Drama"]["May"], genre_per_month["Drama"]["June"], genre_per_month["Drama"]["July"], genre_per_month["Drama"]["August"], genre_per_month["Drama"]["September"], genre_per_month["Drama"]["October"], genre_per_month["Drama"]["November"], genre_per_month["Drama"]["December"]], color='b', linestyle='-')

#plotting the number of movies from horror released each month
plot.plot(months, [genre_per_month["Horror"]["January"], genre_per_month["Horror"]["February"], genre_per_month["Horror"]["March"], genre_per_month["Horror"]["April"], genre_per_month["Horror"]["May"], genre_per_month["Horror"]["June"], genre_per_month["Horror"]["July"], genre_per_month["Horror"]["August"], genre_per_month["Horror"]["September"], genre_per_month["Horror"]["October"], genre_per_month["Horror"]["November"], genre_per_month["Horror"]["December"]], color='orange', linestyle='-')

#plotting the number of movies from action released each month
plot.plot(months, [genre_per_month["Action"]["January"], genre_per_month["Action"]["February"], genre_per_month["Action"]["March"], genre_per_month["Action"]["April"], genre_per_month["Action"]["May"], genre_per_month["Action"]["June"], genre_per_month["Action"]["July"], genre_per_month["Action"]["August"], genre_per_month["Action"]["September"], genre_per_month["Action"]["October"], genre_per_month["Action"]["November"], genre_per_month["Action"]["December"]], color='green', linestyle='-')

#plotting the number of movies from comedy released each month
plot.plot(months, [genre_per_month["Comedy"]["January"], genre_per_month["Comedy"]["February"], genre_per_month["Comedy"]["March"], genre_per_month["Comedy"]["April"], genre_per_month["Comedy"]["May"], genre_per_month["Comedy"]["June"], genre_per_month["Comedy"]["July"], genre_per_month["Comedy"]["August"], genre_per_month["Comedy"]["September"], genre_per_month["Comedy"]["October"], genre_per_month["Comedy"]["November"], genre_per_month["Comedy"]["December"]], color='red', linestyle='-')

#labeling the graph for question 5
plot.ylabel('Number of movies')
plot.xlabel('Month')
plot.title('Number of movies released in different months of 2016')
plot.legend(['Drama','Horror','Action','Comedy'])
plot.savefig("question5-plot.pdf")
plot.show()

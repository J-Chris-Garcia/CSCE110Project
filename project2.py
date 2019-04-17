# CSCE110Project

import csv # import csv module

#initialize number of columns and rows
cols = []
rows = []

#reading csv file
with open ('2016_movie_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    cols = csvreader.next() # getting column names through first row
    
    # getting data from each row one by one
    for row in csvreader:
        rows.append(row)
    # find total number of rows (movies)
    num_rows = csvreader.line_num
    print(f"***********Dataset details************")
    print(f"\n\nNumber of Movies: {num_rows}") #print total number of movies released 
    #create a genre list
    genres = []
    genres = row[3] #fill genre list with data from row index 3 (genre column)
    #create a genre list to be used to count different unique genres 
    diff_genres = []
    
    #update diff_genres list to figure out how many different genres there are in the file
    for n in genres:
        if n not in diff_genres:
            diff_genres.append(n)
    print(f"Number of different genres: {len(diff_genres)}") #print number of different genres
    #create a mpaa ratings list
    mpaa_ratings = []
    mpaa_ratings = row[4] #fill mpaa ratings list with data from row index 4 (ratings column)
    #create a mpaa ratings list to be used to count different unique ratings
    diff_mpaa_ratings = [] 
    
    #update diff_mpaa_ratings list to figure out how many different ratings there are in the file
    for n in mpaa_ratings:
        if n not in diff_mpaa_ratings:
            diff_mpaa_ratings.append(n)
    print(f"Number of different MPAA: {len(diff_mpaa_ratings)}") #print the number of different mpaa ratings
    #create distributors list
    distributors = []
    distributors = row[2] # fill distributor list with data from row index 2 (distributor column)
    #create a distributors list to be used to count different unique distributors
    diff_distributors = [] 
    
    #update diff_distributors list to figure out how many different distributors there are in the file
    for n in distributors:
        if n not in diff_distributors:
            diff_distributors.append(n)
    
    print(f"Number of different distributors: {len(diff_distributors)}") #print the number of different distributors
    tickets_sold = row[5] #fill tickets sold list with data from row index 5 (number of tickets sold for each movie)
    total_tickets_sold = sum(Decimal(i) for i in tickets_sold) #find the sum of the number of tickets sold for all movies in 2016
    
    print(f"Total number of tickets sold: {total_tickets_sold}") #print total number of tickets sold for all movies in 2016
    print("\n\n*************************************")

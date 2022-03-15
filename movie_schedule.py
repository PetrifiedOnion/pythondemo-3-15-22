current_movies = {'The Grinch':'11:00', 'Rudolph':'13:00','Frosty the Snowman':'15:00','Christmas Vacation':'17:00'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie is not playing.")
else:
    print(movie, 'is playing at', showtime)
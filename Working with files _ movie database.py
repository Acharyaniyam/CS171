# YOUR HEADER COMMENT GOES HERE
#Prorammer = Niyam Acharya
#Program date = August 23, 2023
#Program description = Using a movie text file database to get the details of the movie and teh number of movies a databse entails.

# FUNCTION DEFINITIONS
def getFileName():
    """
    Asks the user to enter the name of the data file and validates its existence.
    Returns a string representing the name of a valid file.
    """
    while True:
        file_name = input("Enter name of the data file: ")
        try:
            with open(file_name, "r"):
                return file_name
        except FileNotFoundError:
            print("Error: that file does not exist. Try again.")

def movieFinder(movie_lines, movieTitle):
    """
    Finds a movie in the data file.
    Parameters:
        inFile (file object): A file opened for reading.
        movieTitle (str): The title of the movie to look for.
    Returns:
        tuple: (boolean, int, float) indicating whether the movie was found,
               its running time, and its rating.
               If the movie is not found, (False, 0, 0) is returned.
    """
    for line in movie_lines:
        lines = line.strip().split('\t')
        if lines[0] == movieTitle:
            return True, int(lines[3]), float(lines[4])
    return False, 0, 0

def createReport(movie_lines, genre):
    """
    Creates a report of movies by genre.
    Parameters:
        inFile (file object): A file opened for reading.
        genre (str): The genre of movies to search for.
    Returns:
        int: The number of movies of the given genre found in the data file.
    """
    movie_count = 0
    with open("movieReport.txt", "w") as outFile:
        for line in movie_lines:
            lines = line.strip().split('\t')
            if lines[1].lower() == genre.lower():
                outFile.write(lines[0] + "\n")
                movie_count += 1 
        outFile.write(f"\nGenre: {genre.capitalize()}\n")
        outFile.write(f"Total movies: {movie_count}\n")
    return movie_count

def main():
    
    file_name = getFileName()
    
   
    with open(file_name, "r") as inFile:
        
        movie_lines = inFile.readlines()
        
        title = input("Enter title of a movie: ")
        movie_title = title.capitalize()
        found, running_time, rating = movieFinder(movie_lines, movie_title)
        if found:
            print(f"{movie_title} has a running time of {running_time} minutes and a rating of {rating} stars.")
        else:
            print(f"{movie_title} was not found in the file.")
        
        
        genre = input("What type of movie would you like to watch? ")
        movie_count = createReport(movie_lines, genre)
        print(f"Genre: {genre.capitalize()}\nMovies Found: {movie_count}")


# main script
if __name__ == "__main__":
    main()
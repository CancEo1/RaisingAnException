# Purpose: Demonstrate how to raise an exception in Python.
# Raising an exception for testing an exception handler
def get_movies(filename):
    try:
        with open(filename, newline="") as file:
            raise OSError("OSError: File not found")   # For testing
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except Exception as e:
        print(type(e), e)

# Raising an exception that should be handled by the calling function
def get_movies2(filename):
    if len(filename) == 0:
        raise ValueError("ValueError: Filename cannot be empty")
    with open(filename, newline="") as file:
        movies = []
        reader = csv.reader(file)
        for now in reader:
            movies.append(row)
    return movies

# Logging an exception and raising it for the calling function
def get_movies3(filename):
    try:
        with open(filename, newline="") as file:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except Exception as e:
        log_exception(e)
        raise e
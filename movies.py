class Movies:

    def print_movies(self):
        for i in range(len(self._movies)):
            print(i, "\t", self._movies[i]['name'])
        print()

    def search_names(self, search_string):
        print()
        total_results = 0
        for i in range(len(self._movies)):
            if search_string in self._movies[i]['name'].lower():
                print(self._movies[i]['name'])
                total_results += 1
        if total_results == 0:
            print(f"Sorry, no movies found with the query: '{search_string}'")
        print()
        
    def search_casts(self, search_string):
        print()
        total_results = 0
        for movie in self._movies:
            if search_string in "".join(movie['cast']).lower():
                print(movie['name'])
                total_results += 1
                temp = []
                for actor in movie['cast']:
                    if search_string in actor.lower():
                        temp.append(actor)
                print(temp)
        if total_results == 0:
            print(f"Sorry, no movies found with a cast member named: '{search_string}'")
        print()

    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )

if __name__ == "__main__":
    movies = Movies('./movies.txt')

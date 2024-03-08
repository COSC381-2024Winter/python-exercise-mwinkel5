from movies import Movies

movies = Movies('./movies.txt')

response = ""
while response.lower() != "q":
    print("Program options:\n")
    print("  [L]: List All Movies")
    print("  [N]: Search Movies by Name")
    print("  [Q]: Quit Progam")
    response = input("\nChoose option: ")

    match response.lower():
        case "l":
            movies.print_movies()
        case "n":
            movies.search_names(input("Enter query: ").lower())

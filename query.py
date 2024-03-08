from movies import Movies

movies = Movies('./movies.txt')

response = ""
while response.lower() != "q":
    print("Program options:\n")
    print("  [Q]: Quit Progam")
    response = input("\nChoose option: ")
  

# 1
# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter somthing you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I have't watched that yet")

# 2
number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed currectly!")
    elif number - user_number in (1, -1):
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")
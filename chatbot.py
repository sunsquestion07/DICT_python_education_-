def greet():
    bot_name = "DICT_Bot"
    birth_year = 2025

    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")
def remind_name():
    print(f"Please remind me youre name.")
    name = input()
    print(f"What a great name you have, {name}")
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    remainder3 = int(input("> "))
    remainder5 = int(input("> "))
    remainder7 = int(input("> "))

    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")
import random


def get_winner(player, computer, options):
    if player == computer:
        return "draw"

    index = options.index(player)
    half = len(options) // 2

    weaker_options = []
    for i in range(1, half + 1):
        weaker_options.append(options[(index + i) % len(options)])

    if computer in weaker_options:
        return "win"
    else:
        return "lose"


def get_user_rating(name):
    try:
        with open("rating.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(name + " "):
                    return int(line.split()[1])
    except FileNotFoundError:
        pass
    return 0


def main():
    print("Enter your name:")
    name = input("> ")
    print(f"Hello, {name}")

    rating = get_user_rating(name)

    options_input = input()
    if options_input.strip() == "":
        options = ["rock", "paper", "scissors"]
    else:
        options = options_input.split(",")

    print("Okay, let's start")

    while True:
        user_input = input()

        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {rating}")
            continue
        elif user_input not in options:
            print("Invalid input")
            continue

        computer_choice = random.choice(options)
        result = get_winner(user_input, computer_choice, options)

        if result == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
            rating += 100
        elif result == "draw":
            print(f"There is a draw ({computer_choice})")
            rating += 50
        else:
            print(f"Sorry, but the computer chose {computer_choice}")


if __name__ == "__main__":
    main()
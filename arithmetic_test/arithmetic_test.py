import random


def get_random_operation():
    operations = ['+', '-', '*']
    return random.choice(operations)


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Incorrect format.")


def level1():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = get_random_operation()
    print(f"{num1} {operation} {num2}")
    correct_answer = calculate(num1, num2, operation)
    user_answer = get_integer_input("> ")
    if user_answer == correct_answer:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def level2():
    num = random.randint(11, 29)
    print(num)
    correct_answer = num * num
    user_answer = get_integer_input("> ")
    if user_answer == correct_answer:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def main():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    while True:
        try:
            level = int(input("> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    correct_count = 0

    for i in range(5):
        if level == 1:
            correct_count += level1()
        else:
            correct_count += level2()

    print(f"Your mark is {correct_count}/5.")

    save = input("Would you like to save the result? Enter yes or no.\n> ")

    if save.lower() in ['yes', 'y']:
        name = input("What is your name?\n> ")
        level_desc = "1 (simple operations with numbers 2-9)" if level == 1 else "2 (integral squares of 11-29)"

        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}: {correct_count}/5 in level {level_desc}\n")

        print('The results are saved in "results.txt".')


if __name__ == "__main__":
    main()
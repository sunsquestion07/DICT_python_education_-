def main():
    markdown_result = []

    available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                            "unordered-list", "new-line"]
    special_commands = ["!help", "!done"]

    while True:
        user_input = input("Choose a formatter: ")

        if user_input == "!help":
            print("Available formatters:", " ".join(available_formatters))
            print("Special commands:", " ".join(special_commands))
            continue

        elif user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write("".join(markdown_result))
            print("Result saved to output.md")
            break

        elif user_input not in available_formatters:
            print("Unknown formatting type or command")
            continue

        if user_input == "new-line":
            markdown_result.append("\n")
            print("".join(markdown_result))

        elif user_input == "plain":
            text = input("Text: ")
            markdown_result.append(text)
            print("".join(markdown_result))

        elif user_input == "bold":
            text = input("Text: ")
            markdown_result.append(f"**{text}**")
            print("".join(markdown_result))

        elif user_input == "italic":
            text = input("Text: ")
            markdown_result.append(f"*{text}*")
            print("".join(markdown_result))

        elif user_input == "inline-code":
            text = input("Text: ")
            markdown_result.append(f"`{text}`")
            print("".join(markdown_result))

        elif user_input == "header":
            while True:
                try:
                    level = int(input("Level: "))
                    if 1 <= level <= 6:
                        break
                    else:
                        print("The level should be within the range of 1 to 6")
                except ValueError:
                    print("The level should be within the range of 1 to 6")
            text = input("Text: ")
            markdown_result.append(f"{'#' * level} {text}\n")
            print("".join(markdown_result))

        elif user_input == "link":
            label = input("Label: ")
            url = input("URL: ")
            markdown_result.append(f"[{label}]({url})")
            print("".join(markdown_result))

        elif user_input == "ordered-list":
            while True:
                try:
                    rows = int(input("Number of rows: "))
                    if rows > 0:
                        break
                    else:
                        print("The number of rows should be greater than zero")
                except ValueError:
                    print("The number of rows should be greater than zero")

            list_items = []
            for i in range(1, rows + 1):
                row_text = input(f"Row #{i}: ")
                list_items.append(f"{i}. {row_text}")

            result = "\n".join(list_items) + "\n"
            markdown_result.append(result)
            print("".join(markdown_result))

        elif user_input == "unordered-list":
            while True:
                try:
                    rows = int(input("Number of rows: "))
                    if rows > 0:
                        break
                    else:
                        print("The number of rows should be greater than zero")
                except ValueError:
                    print("The number of rows should be greater than zero")

            list_items = []
            for i in range(1, rows + 1):
                row_text = input(f"Row #{i}: ")
                list_items.append(f"* {row_text}")

            result = "\n".join(list_items) + "\n"
            markdown_result.append(result)
            print("".join(markdown_result))


if __name__ == "__main__":
    main() 
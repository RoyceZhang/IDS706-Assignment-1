def welcome_message(name):
    name = name.strip()

    if not name:
        return "Welcome to the Data Engineering course."

    return f"{name}, welcome to the Data Engineering course."


def main():
    name = input("Enter your name: ")
    print(welcome_message(name))


if __name__ == "__main__":
    main()

import sys


def print_beatiful(text):
    for letter in text:
        print(letter, end="")
        sys.sleep(0.1)
    print()


def main():
    print_beatiful("I want to lick")
    pass


if __name__ == "__main__":
    main()

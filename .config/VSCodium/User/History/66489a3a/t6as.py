import time


def print_beatiful(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.03)
    print()


def main():
    print_beatiful("I want to lick")


if __name__ == "__main__":
    main()

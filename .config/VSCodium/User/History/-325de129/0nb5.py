"""
module which copies functionality of ls -r
"""
import os
import argparse


def print_dirs(tmp_root, count=0, branches=0):
    for root, dirs, files in os.walk(tmp_root):
        print(root)
        print(dirs)
        print(files)
        to_print = sorted(dirs + files)
        for node in to_print:
            if branches:
                print(branches * "│  " + (count - 1) * "   ", end = "")
            elif count:
                print("   " * count, end="")
            if node == to_print[-1]:
                print("└──", node)
            else:
                print("├──", node)

            if node in dirs:
                if node != to_print[-1]:
                    print_dirs(node, count + 1, branches + 1)
                else:
                    print_dirs(node, count + 1)
                    

        break


def main():
    """
    recursively writes out all directories and files
    """
    parser = argparse.ArgumentParser(
        prog="ls -r",
        description="recursively writes dirs and subdirs",
    )

    parser.add_argument("--dir", type=str, default="./test")

    args = parser.parse_args()

    try:
        while args.dir[-1] == "/":
            args.dir = args.dir[:-1]

        args.dir += "/"

        print(os.getcwd())

        print(args.dir)
        for root, dirs, files in os.walk(args.dir):
            print(root, dirs, files)
        print_dirs(args.dir)

    except FileNotFoundError as err:
        print(err)
        return err


if __name__ == "__main__":
    main()

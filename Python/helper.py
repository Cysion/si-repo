#!/usr/bin/python
import json
import os
import shutil

#built on python 3.7.4, version incompatabilities may occur

def main() -> bool:
    with open("index.json", "r") as infile:
        exercises = json.load(infile)
    choice = menu(exercises)
    if choice:
        try:
            nice_print(choice, exercises[choice])
            input()
        except KeyError:
            print("The category you entered does not exist! try another one")
            input()
        except Exception:
            print("An unexpected error has occured! Behave next time")
            input()
        finally:
            return 1
    else:
        return 0


def nice_print(category: str, exercises: list) -> None:
    x, y = getsize()
    clear()
    print(f'In the category "{category}" are the following exercises:'.center(x, " "))
    for exercise in exercises:
        print(f" - {exercise}".center(x, " "))
    

def menu(exercises: dict) -> str or bool:
    x, y = getsize()
    print(f'Welcome to the SI exercise helper! Below are listed different categories with exercises you can do!'.center(x, "-"))
    for category in exercises:
        print(f"{category}: {len(exercises[category])} exercises".center(x, " "))
    print('Please enter the name of a category to know what kind of exercises are in it! Or enter "quit" to exit the helper'.center(x, "-"))
    choice = input(" > ")
    if choice != "exit":
        return choice
    else:
        return 0

    
def getsize() -> tuple:
    try:
        x, y = shutil.get_terminal_size()
    except Exception:
        x, y = 10, 10
    return x, y

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear()
    while main():
        clear()
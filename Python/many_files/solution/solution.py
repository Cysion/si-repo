#!/usr/bin/python
import os
import sys
sys.setrecursionlimit(10000)

def main():
    paths = pathfinder("files", [])
    number = calcer(paths)
    print(number)

def pathfinder(path: str, paths: list) -> list:
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            paths += pathfinder(item_path, paths)
        else:
            paths.append(item_path)
    return paths

def calcer(paths: list) -> int:
    sum_these = []
    sub_these = []
    mult_these = []
    total = int()
    for path in paths:
        name = path.split("/")[-1]
        if name[0].isalpha():
            sum_these.append(path)
        elif int(name[0])%2 != 0:
            sub_these.append(path)
        else:
            mult_these.append(path)
    for path in sum_these:
        total+=get_num(path)

    for path in sub_these:
        total-=get_num(path)

    total*=len(mult_these)
    
    return total

def get_num(path: str) -> int:
    number = int()
    with open(path, "r") as infile:
        number = int(infile.read())
    return number

if __name__ == "__main__":
    main()
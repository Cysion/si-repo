#!/usr/bin/python
import random
import os

random.seed(24601)
FILE_COUNTER = 0

def main():
    depth = random.randint(2,3)
    start_dir = "solution/files"
    maker_man(depth, start_dir)
    

def maker_man(depth_left: int, current_path: str) -> None:
    global FILE_COUNTER
    if depth_left:
        for dirnum in range(random.randint(1,3)):
            next_path = os.path.join(current_path, f"directory{dirnum}")
            os.mkdir(next_path)
            maker_man(depth_left-1, next_path)
            
    for i in range(random.randint(2,4)):
        with open(os.path.join(current_path, random_string()), "w") as outfile:
            outfile.write(str(random.randint(0,9999999)))
            FILE_COUNTER += 1
        

def random_string():
    choose_from = "abcdefghij0123456789"
    randstring = str()
    for i in range(random.randint(3,6)):
        randstring += random.choice(choose_from)
    return randstring

if __name__ == "__main__":
    main()
    print(FILE_COUNTER, " files made")
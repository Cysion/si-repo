import random
with open("numbers.txt", "w") as of:
    for i in range(1024):
        num = random.randint(0,4192)
        of.write(str(num) + "\n")
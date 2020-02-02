import os
import time
COMPILE_CMD = "g++ -O0 "
from statistics import mean as m

def compile_all():
    competitors = dict()
    for competitor in os.listdir("competitor_source"):
        tmp = competitor.split(".")
        tmp = tmp[0]
        competitors[tmp] = []
        os.system(f"{COMPILE_CMD} competitor_source/{competitor} -o competitor_exec/{tmp}")
    return competitors


def cycle(competitors):
    for competitor in competitors:
        time1 = time.time()
        os.system(f"./competitor_exec/{competitor}")
        time2 =  time.time() - time1
        competitors[competitor].append(time2)
    return competitors


def compile_results(competitors):
    for competitor in competitors:
        print(f"{competitor} got an average time of {m(competitors[competitor])}")


def main():
    turns = int(input("how many cycles? "))
    competitors = compile_all()
    for i in range(turns):
        competitors = cycle(competitors)
    compile_results(competitors)


if __name__ == "__main__":
    main()
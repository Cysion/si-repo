from obj.Grid import Grid
import time
import shutil

def neighbours(grid: Grid, x: int, y: int, incl = False) -> int:
        neighbours = []
        lenx = len(grid.matrix[y]) - 1
        leny = len(grid.matrix) - 1

        if (x > 0) and (y > 0):
            neighbours.append(grid.matrix[y - 1][x - 1])

        if y > 0:
            neighbours.append(grid.matrix[y - 1][x])

        if (y > 0) and (x < lenx):
            neighbours.append(grid.matrix[y - 1][x + 1])

        if x > 0:
            neighbours.append(grid.matrix[y][x - 1])

        if incl:
            neighbours.append(grid.matrix[y][x])

        if x < lenx:
            neighbours.append(grid.matrix[y][x + 1])

        if (y < leny) and (x > 0):
            neighbours.append(grid.matrix[y + 1][x - 1])

        if y < leny:
            neighbours.append(grid.matrix[y + 1][x])

        if (y < leny) and (x < lenx):
            neighbours.append(grid.matrix[y + 1][x + 1])

        return neighbours

def gollogic(grid, stats = [0, 0, 0, 0, 0, 0 ,0]):
    t0 = time.time()
    yc = 0
    rgrid = Grid(" ", "0")
    births = 0
    deaths = 0
    rgrid.make(len(grid.matrix[0]), len(grid.matrix))
    for y in grid.matrix:
        xc = 0
        for x in y:
            n = grid.neighbours(xc, yc, False)
            xcount = n.count(grid.occ)

            if (xcount < 2) and x == grid.occ:
                rgrid.matrix[yc][xc] = grid.emp
                deaths += 1

            elif ((xcount == 2) or (xcount == 3)) and x == grid.occ:
                rgrid.matrix[yc][xc] = grid.occ

            elif (xcount > 3) and x == grid.occ:
                rgrid.matrix[yc][xc] = grid.emp
                deaths += 1

            elif (x == grid.emp) and (xcount == 3):
                rgrid.matrix[yc][xc] = grid.occ
                births += 1

            xc += 1
        yc += 1
    stats[0] = births
    stats[1] = deaths
    stats[2] += births
    stats[3] += deaths
    stats[5] += 1
    stats[6]=round((1/(time.time()-t0)), 1)
    return rgrid.matrix, stats

if __name__ == "__main__":
    grid = Grid(" ", "0")
    x, y = shutil.get_terminal_size()
    grid.make(x, y)
    grid.rfill()
    while 1:
        time.sleep(0.1)
        grid.print()
        grid.matrix, grid.stats = gollogic(grid, stats=grid.stats)
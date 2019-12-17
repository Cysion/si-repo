from obj.Grid import Grid
import time
import shutil

def gollogic(grid: Grid, stats = [0, 0, 0, 0, 0, 0, 0]) -> (list, list):


    #stub code, needs to be changed!
    updated_matrix = grid.matrix
    updated_stats = grid.stats
    return updated_matrix, updated_stats


if __name__ == "__main__":
    grid = Grid(" ", "0")
    try:
        x, y = shutil.get_terminal_size()
    except:
        x = 20
        y = 20
    grid.make(x, y)
    grid.rfill()
    while 1:
        time.sleep(0.1)
        grid.print()
        grid.matrix, grid.stats = gollogic(grid, stats=grid.stats)

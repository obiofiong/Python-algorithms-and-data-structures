def islandPerimeter( grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    island_coordinates = []
    # for row in grid:
    #     for cell in row:
    #         if cell == 1:
    #             island_coordinates.append()
    perimeter = 0
        
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] :
                perimeter +=4
                if i > 0 and grid[i - 1][j]:
                        perimeter -= 2
                if j > 0 and grid[i][j - 1]:
                    perimeter -= 2

    return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
islandPerimeter(grid)
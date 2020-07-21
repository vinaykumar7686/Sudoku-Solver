class Solve():
    def __init__(self, grid):
        self.grid = grid

    def printSol(self):
        hsep1 = " _____ _____ _____ "
        hsep2 = "|     |     |     |"
        hsep3 = "|  {}  |  {}  |  {}  |"
        hsep5 = "|_____|_____|_____|"
        
        l12 = hsep1*3+"\n"+hsep2*3
        l3 = (hsep3*3)
        l4 = hsep5*3
        
        r147 = l12+"\n"+l3+"\n"+l4
        ro = hsep2*3+"\n"+(hsep3*3)+"\n"+hsep5*3

        glayout = (r147+"\n"+ro+"\n"+ro+"\n")*3

        #print(f'{glayout.format(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9)}')
        gr = [y for x in self.grid for y in x]
        print(glayout.format(*gr))

    def isValid(self, x, y, num):
        def isValidRow():
            '''
            Tested OK
            '''
            if num in self.grid[x][:]:
                return False
            return True
        
        def isValidCol():
            '''
            Tested OK
            '''
            if num in [x[y] for x in self.grid]:
                return False
            return True

        def isValidBlock():
            '''
            Tested OK
            '''
            rlb = 3*(x//3)
            rub = rlb+3
            clb = 3*(y//3)
            cub = clb+3

            li = []
            [li.extend(x[clb:cub]) for x in self.grid[rlb:rub]]

            if num in li:
                return False
            return True

        if isValidBlock() and isValidCol() and isValidRow():
            return True
        else:
            return False

    def solve(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.grid[i][j] == 0:
                    for k in range(1,10):
                        if self.isValid(i, j, k):
                            self.grid[i][j] = k
                            self.solve()
                            self.grid[i][j] = 0
                    return

        self.printSol()

if __name__ == "__main__":
    grid = [
        [0,0,0,9,0,4,6,0,0],
        [0,4,0,0,0,0,8,3,1],
        [8,2,0,6,1,0,0,0,0],
        [0,9,0,8,3,2,1,0,7],
        [2,1,8,7,4,5,0,0,0],
        [7,0,3,0,0,6,0,0,0],
        [0,0,2,0,0,0,4,0,0],
        [1,8,5,4,2,9,0,6,0],
        [3,7,0,0,0,0,0,2,0]
        ]
    ss = Solve(grid)
    print(ss.solve())


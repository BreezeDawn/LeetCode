class Num695(object):
    def __init__(self):
        self.dic = {0: 0}
        self.ls = []
        self.num = 0
        self.area = 1

    def leetcode(self, grid):
        sign = 0
        self.grid = grid
        for i, j in enumerate(self.grid):
            for m, n in enumerate(j):
                self.wheel(i, m, n, sign)
        return max(self.dic.values())

    def wheel(self, i, m, n, sign):
        if (not n) or ([i, m] in self.ls):
            return
        self.ls.append([i, m])
        if not sign:
            self.num += 1
            self.dic[self.num] = self.area
            self.area = 1
        else:
            self.area += 1
            self.dic[self.num] = self.area
        if m != 0:
            self.wheel(i, m - 1, self.grid[i][m - 1], 1)
        if i != 0:
            self.wheel(i - 1, m, self.grid[i - 1][m], 1)
        if m + 1 != len(self.grid[i]):
            self.wheel(i, m + 1, self.grid[i][m + 1], 1)
        if i + 1 != len(self.grid):
            self.wheel(i + 1, m, self.grid[i + 1][m], 1)


def main():
    tmp = Num695()
    max_area = tmp.leetcode([[0]])
    print(max_area)


if __name__ == '__main__':
    main()

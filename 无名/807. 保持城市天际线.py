class Num807(object):
    @staticmethod
    def leetcode(grid):
        self_max = []
        index_max = []
        k = 0
        num = 0
        res = 0
        for i in range(len(grid)):
            self_max.append(max(grid[i]))
            for j in grid:
                k = max(j[num], k)
            index_max.append(k)
            num += 1
            k = 0
        for i in range(len(self_max)):
            for j in range(len(index_max)):
                res = res + (min(self_max[i], index_max[j]) - grid[i][j])
        return res


def main():
    tmp = Num807.leetcode([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
    print(tmp)


if __name__ == '__main__':
    main()

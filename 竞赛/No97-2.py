# 在R行C列的矩阵上，我们从(r0, c0)
# 面朝东面开始
# 这里，网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。
# 现在，我们以顺时针按螺旋状行走，访问此网格中的每个位置。
# 每当我们移动到网格的边界之外时，我们会继续在网格之外行走（但稍后可能会返回到网格边界）。
# 最终，我们到过网格的所有R * C个空间。
# 按照访问顺序返回表示网格位置的坐标列表。
# 示例1：
# 输入：R = 1, C = 4, r0 = 0, c0 = 0
# 输出：[[0, 0], [0, 1], [0, 2], [0, 3]]
# 示例2：
# 输入：R = 5, C = 6, r0 = 1, c0 = 4
# 输出：[[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2],
#     [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0],
#     [1, 0], [0, 0]]
# 提示：
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C


class Numgame2(object):
    @staticmethod
    def leetcode(R, C, r0, c0):
        index_y = r0
        index_x = c0 + 1
        num = max(R,C)
        count = 2
        ls = []
        res = []
        while num:
            ls.append((index_y,index_x))
            index_y -= 1
            index_x += 1
            num -= 1
        for j,i in enumerate(ls):
            res.append(i)
            y = i[0]
            x = i[1]
            for i in range(count-1):
                y += 1
                res.append((y,x))
            for i in range(count):
                x -= 1
                res.append((y,x))
            for i in range(count):
                y -= 1
                res.append((y,x))
            for i in range(count):
                x += 1
                res.append((y,x))
            count += 2
            res_res = []
            for i in res:
                if i[0]>=R or i[1]>=C or i[0]<0 or i[1]<0:
                    continue
                res_res.append(i)
            res_res.insert(0,(r0,c0))
        return res_res




def main():
    tmp = Numgame2.leetcode(R = 1, C = 4, r0 = 0, c0 = 0)
    print(tmp)


if __name__ == '__main__':
    main()

# 给定两个句子A和B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
# 返回所有不常用单词的列表。
# 您可以按任何顺序返回列表。
# 示例1：
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet", "sour"]
# 示例2：
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]
# 提示：
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A和B
# 都只包含空格和小写字母。


class Numgame01(object):
    @staticmethod
    def leetcode(A,B):
        ls = []
        for i in A.split():
            if i not in B.split() and A.split().count(i) == 1:
                ls.append(i)
        for i in B.split():
            if i not in A.split() and B.split().count(i) == 1:
                ls.append(i)
        return ls



def main():
    tmp = Numgame01.leetcode("op vu kux dn jsenj hbdez hbdez nbenh z op dxmqd op","kux wnx wnx wbi jsenj nlgfn vu f vu fvxas dn op tb")
    print(tmp)


if __name__ == '__main__':
    main()

class Num583(object):
    @staticmethod
    def leetcode(word1, word2):
        new_1 = ''
        new_2 = ''
        res = 0
        for i in word1:
            if i in word2:
                new_1 += i
        for i in word2:
            if i in word1:
                new_2 += i
        return new_1,new_2




def main():
    tmp = Num583.leetcode("eewrca", "aeswgc")
    print(tmp)


if __name__ == '__main__':
    main()

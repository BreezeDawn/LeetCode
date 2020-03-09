class Num345(object):
    @staticmethod
    def leetcode(s):
        vowel = ('a','e','i','o','u')
        res = list(s)
        vo_list = []
        for i in s:
            if i.lower() in vowel:
                vo_list.append(i)
        for i,j in enumerate(res):
            if j.lower() in vowel:
                res[i] = vo_list.pop()
        return ''.join(res)


def main():
    tmp = Num345.leetcode("leetcode")
    print(tmp)


if __name__ == '__main__':
    main()

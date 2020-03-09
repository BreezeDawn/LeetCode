class Num824(object):
    @staticmethod
    def leetcode(S):
        res = []
        vowel = ('a', 'e', 'i', 'o', 'u')
        slist = S.split(' ')
        for i, j in enumerate(slist):
            if j[0].lower() in vowel:
                res.append(j + 'ma' + (i + 1) * 'a')
                continue
            res.append(j[1:] + j[0] + 'ma' + (i + 1) * 'a')
        return ' '.join(res)


def main():
    tmp = Num824.leetcode("I speak Goat Latin")
    print(tmp)


if __name__ == '__main__':
    main()

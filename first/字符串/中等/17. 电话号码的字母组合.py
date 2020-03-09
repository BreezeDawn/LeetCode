class Num17(object):
    def leetcode(self, digits):
        if not digits:
            return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = ['']
        for i in digits:
            self.deep(dic[i])
        return self.res

    def deep(self, i):
        tmp = []
        for x in self.res[:]:
            for y in i:
                tmp.append(x + y)
        self.res = [x for x in tmp]


def main():
    tmp = Num17()
    print(tmp.leetcode('234'))


if __name__ == '__main__':
    main()

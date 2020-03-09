class Num125(object):
    @staticmethod
    def leetcode(s):
        str = s.lower()
        j = len(str) - 1
        for i in str:
            if (not i.isalpha()) and (not i.isalnum()):
                continue
            while (not str[j].isalpha()) and (not str[j].isalnum()):
                j -= 1
            if i != str[j]:
                return False
            j -= 1
        return True


def main():
    tmp = Num125.leetcode("race a car")
    print(tmp)


if __name__ == '__main__':
    main()

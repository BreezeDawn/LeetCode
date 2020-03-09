class Num20(object):
    @staticmethod
    def leetcode(s):
        s_ls = list()
        left = '{[('
        right = '}])'
        for i in s:
            if i in left:
                s_ls.append(i)
            else:
                if not s_ls:
                    return False
                if right.index(i) == left.index(s_ls.pop()):
                    continue
                return False
        else:
            if not s_ls:
                return True
            return False


def main():
    tmp = Num20.leetcode("[")
    print(tmp)


if __name__ == '__main__':
    main()

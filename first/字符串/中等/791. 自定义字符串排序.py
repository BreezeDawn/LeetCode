class Num791(object):
    @staticmethod
    def leetcode(S, T):
        s = list(S)
        t = list(T)
        for i in set(t):
            if i not in s:
                s.append(i)
        t.sort(key=s.index)
        return ''.join(t)


def main():
    tmp = Num791.leetcode("cba", "abcd")
    print(tmp)


if __name__ == '__main__':
    main()

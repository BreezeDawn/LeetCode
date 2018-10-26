class Num443(object):
    @staticmethod
    def leetcode(chars):
        cut = chars[:]
        ls = []
        num = 1
        for i, j in enumerate(cut[:]):
            if i == len(cut) - 1:
                pass
            elif j == cut[i + 1]:
                chars.pop(0)
                num += 1
                continue
            ls.append(chars.pop(0))
            if num != 1:
                for k in repr(num):
                    ls.append(k)
                num = 1
        for i in ls:
            chars.append(i)
        return len(chars)


def main():
    tmp = Num443.leetcode(["a", "b", "b"])
    print(tmp)


if __name__ == '__main__':
    main()

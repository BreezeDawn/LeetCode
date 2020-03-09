class Num66(object):
    @staticmethod
    def leetcode(digits):
        ls = digits[::-1]
        for i,j in enumerate(ls):
            j+=1
            if j == 10:
                ls[i] = 0
                if ls.count(0) == len(ls):
                    ls.append(0)
                continue
            ls[i] += 1
            break
        return ls[::-1]



def main():
    tmp = Num66.leetcode([99])
    print(tmp)


if __name__ == '__main__':
    main()
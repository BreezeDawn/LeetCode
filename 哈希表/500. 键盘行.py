class Num500(object):
    @staticmethod
    def leetcode(words):
        q = 'qwertyuiop'
        a = 'asdfghjkl'
        z = 'zxcvbnm'
        res = []
        for i in words:
            k = i.lower()
            i_num = 0
            for j in q:
                if j in k:
                    i_num += 1
                    break
            for x in a:
                if x in k:
                    i_num += 1
                    break
            if i_num > 1:
                continue
            for y in z:
                if y in k:
                    i_num += 1
                    break
            if i_num > 1:
                continue
            res.append(i)
        return res

def main():
    tmp = Num500.leetcode(["abdfs","cccd","a","qwwewm"])
    print(tmp)


if __name__ == '__main__':
    main()

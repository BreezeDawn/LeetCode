# 需要二叉树才可以运行
class Num606(object):
    @staticmethod
    def leetcode(self, t):
        if not t:
            return ''
        res = []
        return ''.join(self.tree3str(t, res))

    def tree3str(self, t, res):
        if not t:
            return None
        res.append(str(t.val))
        if t.left or t.right:
            res.append('(')
            self.tree3str(t.left, res)
            res.append(')')
        if t.right:
            res.append('(')
            self.tree3str(t.right, res)
            res.append(')')
        return res


def main():
    tmp = Num606()
    print(tmp)


if __name__ == '__main__':
    main()

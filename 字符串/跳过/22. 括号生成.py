# 深层递归
class Num22(object):
    def leetcode(self, n):
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)


def main():
    tmp = Num22()
    tmp = tmp.leetcode(3)
    print(tmp)


if __name__ == '__main__':
    main()


# class Num22(object):
#     @staticmethod
#     def leetcode(n):
#         res = []
#         root = ('(', 1, 0)
#         queue = [root]
#         while len(queue) > 0:
#             curr, op, cl = queue.pop(0)
#             if len(curr) == 2 * n:
#                 res.append(curr)
#             left = curr + '('
#             right = curr + ')'
#             if op + 1 <= n:
#                 queue.append((left, op + 1, cl))
#             if cl + 1 <= op:
#                 queue.append((right, op, cl + 1))
#         return res
#
#
# def main():
#     tmp = Num22.leetcode()
#     print(tmp)


if __name__ == '__main__':
    main()

# 此方法超时,需使用KMP算法

# class Num459(object):
#     @staticmethod
#     def leetcode(s):
#         length = len(s)
#         wh = length//2
#         num = 1
#         while wh:
#             if s.count(s[:num]) == 1:
#                 return False
#             if s.count(s[:num])*num == length:
#                 return True
#             num += 1
#             wh -= 1
#         return False
#
#
#
# def main():
#     tmp = Num459.leetcode("abcabc")
#     print(tmp)
#
#
# if __name__ == '__main__':
#     main()

class Num537(object):
    @staticmethod
    def leetcode(a,b):
        num_ls = []
        cpx_ls = []
        a = a.split('+')
        b = b.split('+')
        for i in a :
            for j in b:
                if ('i'in i )and ('i' in j):
                    num_ls.append(-1*eval(i[:-1])*eval(j[:-1]))
                    continue
                elif 'i'in i:
                    cpx_ls.append(eval(i[:-1])*eval(j))
                elif 'i' in j:
                    cpx_ls.append(eval(i)*eval(j[:-1]))
                else:
                    num_ls.append(eval(i)*eval(j))
        return str(sum(num_ls))+'+'+str(sum(cpx_ls))+'i'



def main():
    tmp = Num537.leetcode("1+1i", "1+1i")
    print(tmp)
    tmp2 = Num537.leetcode("1+-1i", "1+-1i")
    print(tmp2)


if __name__ == '__main__':
    main()

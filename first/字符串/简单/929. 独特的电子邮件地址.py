class Num929(object):
    @staticmethod
    def leetcode(emails: list) -> int:
        result = set()
        for email in emails:
            el = email.split("@")
            result.add(el[0].split("+")[0].replace(".", "") + el[1])
        return len(result)


def main():
    tmp = Num929.leetcode(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])
    print(tmp)


if __name__ == '__main__':
    main()

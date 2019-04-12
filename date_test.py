import unittest
from date import parse


class ParseTests(unittest.TestCase):
    def test_split(self):
        self.assertEqual(parse("1/2/3"), "2001-02-03")
        self.assertEqual(parse("3/20/1"), "2001-03-20")
        self.assertEqual(parse("2010/5/2"), "2010-02-05")
        self.assertEqual(parse("10/99/2"), "2099-02-10")
        self.assertEqual(parse("2010/99/2"), "is illegal")
        self.assertEqual(parse("2010/5/2000"), "is illegal")
        self.assertEqual(parse("2019/2/29"), "is illegal")
        self.assertEqual(parse("2020/2/29"), "2020-02-29")
        self.assertEqual(parse("19/2/29"), "2029-02-19")
        self.assertEqual(parse("20/2/29"), "2020-02-29")
        self.assertEqual(parse("0/1/2"), "2000-01-02")
        self.assertEqual(parse("0/0/2"), "is illegal")


if __name__ == '__main__':
    unittest.main()

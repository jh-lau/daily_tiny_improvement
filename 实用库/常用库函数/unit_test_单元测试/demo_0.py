"""
  @Author       : liujianhan
  @Date         : 2020/11/4 11:37
  @Project      : DailyTinyImprovement
  @FileName     : demo_0.py
  @Description  : Placeholder
"""
import unittest


class TestStringMethods(unittest.TestCase):
    def test_uppper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello worlds'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

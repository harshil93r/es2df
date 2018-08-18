import unittest
from es2df.error import IndexRequired
from es2df import ES2DF


class TestES2DF(unittest.TestCase):

    def test_index_not_given(self):
        with self.assertRaises(IndexRequired) as e:
            es2df_obj = ES2DF()
            es2df_obj.to_df()
        # print(e.message)

    def test_index_not_found(self):
        with self.assertRaises(IndexRequired) as e:
            es2df_obj = ES2DF(index='random_index_value')
            es2df_obj.to_df()
        # print(str(e))
        # self.assertEqual(first, second)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''
    def test_register_params_check(self):
        self.assertEqual(register_params_check(None), ("ok", True))


if __name__ == '__main__':
    unittest.main()

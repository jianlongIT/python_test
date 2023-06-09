# -*- coding: utf-8 -*-
# Auther : jianlong
from newrooro import Newerror


def test():
    try:
        assert 1 > 2, '发生错误'
        raise Newerror("跑出一个异常")
    except AssertionError as e:
        print(e)
    except Newerror as e:
        print(e)
    finally:
        print('finally')


test()

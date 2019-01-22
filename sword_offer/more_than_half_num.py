# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The more_than_half_num file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution(object):
    def MoreThanHalfNum_Solution(self, numbers):
        cnt = 0
        num = None
        for x in numbers:
            if cnt == 0:
                num = x
                cnt += 1
            else:
                if x == num:
                    cnt += 1
                else:
                    cnt -= 1

        c = 0
        for x in numbers:
            if x == num:
                c += 1
        if c >= len(numbers) // 2 + 1:
            return num
        else:
            return 0


if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([4,2,4,1,4,2]))
# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 149_Max_Points_on_a_Line file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

"""


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0

        res = 0
        n = len(points)
        for i in range(n):
            same_pointers = 0
            counter = {}
            for j in range(i + 1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    # 重合的点
                    same_pointers += 1
                else:
                    slope = self._get_slope(points[i], points[j])
                    if slope not in counter:
                        counter[slope] = 0
                    counter[slope] += 1
            ans = same_pointers + max(counter.values()) if counter else same_pointers
            res = max(res, ans)

        return res

    def _get_slope(self, p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y

        # 1. 水平
        if dy == 0:
            return (p1.y, 0)
        # 2. 垂直
        if dx == 0:
            return (0, p1.x)
        d = self.gcd(dx, dy)
        return (dy / d, dx / d)

    def gcd(self, m, n):
        return m if n == 0 else self.gcd(n, m % n)


if __name__ == '__main__':
    points = []
    for a, b in [[1, 1], [2, 2], [3, 3]]:
        points.append(Point(a, b))
    print(Solution().maxPoints(points))

# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 31_use_descriptors_for_reusable_property_method file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        self._value = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None: return self
        return self._value.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self._value[instance] = value


class Exam(object):
        math_grade = Grade()
        writing_grade = Grade()


if __name__ == '__main__':
    first_exam = Exam()
    first_exam.math_grade = 100

    second_exam = Exam()
    second_exam.math_grade = 1

    print first_exam.math_grade

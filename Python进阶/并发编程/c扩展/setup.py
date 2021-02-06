#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 下午2:51
# @Author  : Huanghl
# @Email    : huanghailong@dataexa.com
# @Description:
from distutils.core import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize("cython_test1.pyx"))

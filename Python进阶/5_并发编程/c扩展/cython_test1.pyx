#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 下午2:45
# @Author  : Huanghl
# @Email    : huanghailong@dataexa.com
# @Description: python setup.py build_ext --inplace

cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)

def primes(int kmax):
    cdef int n, k, i
    cdef int p[1000]
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result

def calc_distance(point1, point2):
    res = sum(map(lambda x: (x[0] - x[1]) * (x[0] - x[1]), zip(point1, point2)))
    return res ** 0.5

cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef calc_distance1(point1, point2):
    res = 0
    for i in range(min(len(point1), len(point2))):
        res += (point1[i]-point2[i])*(point1[i]-point2[i])
    return res**0.5

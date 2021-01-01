"""
  @Author       : liujianhan
  @Date         : 2020/11/2 14:17
  @Project      : DailyTinyImprovement
  @FileName     : setup.py
  @Description  : Placeholder
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    # ext_modules=cythonize('hello_world.pyx')
    # 要生成html可视化文件，确保之前生成的.c和.so文件被删除
    ext_modules=cythonize(['primes.pyx',
                           'primes_cpp.pyx',
                           'primes_py_cy.py'], annotate=True)
)

# python setup.py build_ext --inplace

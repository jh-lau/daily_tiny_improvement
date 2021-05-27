import os
import shutil
import zipfile
from distutils.core import setup
from shutil import ignore_patterns

from Cython.Build import cythonize


def run_unit_test(test_file_name='unit_test.py'):
    """
    从父目录查找单元测试文件并逐一测试，TODO 有bug
    :param test_file_name: test file.
    :return:
    """
    import unittest
    parent = os.path.dirname(os.getcwd())
    test_files = []  # 单元测试
    uinit_test_files = []  # 普通测试
    for path, dirs, files in os.walk(parent):
        for file in files:
            if file == test_file_name:
                uinit_test_files.append(os.path.join(path, test_file_name))
    errors = 0
    for file in uinit_test_files:
        word_dir = os.path.dirname(file)
        os.chdir(word_dir)
        loader = unittest.TestLoader()
        suite = loader.discover(word_dir, pattern=test_file_name)
        runner = unittest.TextTestRunner()
        res = runner.run(suite)
        errors += len(res.errors)
        if errors:
            raise EOFError('测试不通过。')
    for file in test_files:
        word_dir = os.path.dirname(file)
        os.chdir(word_dir)
        with open(file, 'r') as tf:
            exec(tf.read())
    # 切换回当前目录
    os.chdir(parent)


def read_ignore_config(file):
    patterns = {'.idea', '.git', '__pycache__'}
    if os.path.exists(file):
        with open(file, 'r') as ignore_f:
            for pattern in ignore_f.readlines():
                pattern = pattern.strip()
                if len(pattern) == 0 or pattern.startswith('#'):
                    continue
                pattern = pattern[:-1] if pattern.endswith(os.path.sep) else pattern
                patterns.add(pattern)

    return ignore_patterns(*patterns)


def copy_dirs(src, dst, ignore_config='.gitignore'):
    dst_path = os.path.join(dst if dst else src, os.path.basename(src))
    # 移除新目录文件
    if os.path.exists(dst_path):
        if dst is None:
            raise IOError("当前项目下存在与项目名称相同的文件夹:%s。无法进行编译，需手动设置其他编译工作目录。" % os.path.basename(dst_path))
        shutil.rmtree(dst_path)
    ignore = read_ignore_config(ignore_config)
    shutil.copytree(src, dst_path, ignore=ignore)
    return dst_path


def encryption(target_dir, exclude_files=None):
    """

    :param target_dir: 待加密的项目目录
    :param exclude_files: 不需要加密的文件列表
    :return:
    """

    # 编译的文件列表
    if exclude_files is None:
        exclude_files = ['service.py', 'unpack_plus.py']
    encrypted_file = []
    for path, dirs, files in os.walk(target_dir):
        if any([file.endswith('.py') for file in files]):
            exclude_file_paths = []
            if '__init__.py' not in files:
                init_file = os.path.join(path, '__init__.py')
                files.append('__init__.py')
                os.mknod(init_file)
            for file in files:
                if file in exclude_files:
                    exclude_file_paths.append(os.path.join(path, file))
            # 生成so文件
            setup(ext_modules=cythonize(os.path.join(path, "*.py"),
                                        exclude=exclude_file_paths),
                  script_args=['build_ext', '-b', os.path.dirname(target_dir)])
            for file in files:
                if file.endswith('.py') and file not in exclude_files:
                    encrypted_file.append(os.path.join(path, file.replace('.py', '.c')))
                    encrypted_file.append(os.path.join(path, file))

    # 删除.c文件和.py文件
    for file in encrypted_file:
        os.remove(file)


def make_zip(dirname):
    """
    压缩包放于同级目录
    :param dirname: 打包的目录
    :return:
    """
    name = dirname + '.zip'
    pre_len = len(os.path.dirname(dirname))
    with zipfile.ZipFile(name, 'w') as z:
        for root, dirs, files in os.walk(dirname):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = file_path[pre_len:].strip(os.path.sep)  # 相对路径
                z.write(file_path, arcname)


def main(project_dir=None, dst=None, remove=True, ignore='.gitignore',
         exclude_files=None,
         unit_test_name=None):
    """

    :param project_dir: 待加密打包的项目目录, 默认为os.getcwd()
    :param dst: 编译加密的文件夹放置目录，默认在当前项目下创建同名文件夹进行加密编译
    :param remove: 是否移除加密后的项目文件夹，仅保留压缩文件
    :param ignore: 忽略文件, 默认和service.py同级下的.gitignore文件, 内置忽略'.idea', '.git', '__pycache__'三种文件夹
    :param exclude_files:
    :param unit_test_name: 测试程序文件, 不为空时执行测试脚本
    :return:
    """
    if exclude_files is None:
        exclude_files = ['service.py', 'unpack_plus.py', 'openapi_init.py', '_metadata.py', '__init__.py']
    if unit_test_name is not None:
        run_unit_test(unit_test_name)
    if project_dir is None:
        project_dir = os.getcwd()
    remove_dir = [os.path.abspath('build')]
    target_item = copy_dirs(src=project_dir, dst=dst, ignore_config=ignore)
    encryption(target_item, exclude_files=exclude_files)
    make_zip(target_item)
    if remove:
        remove_dir.append(target_item)
    for r_dir in remove_dir:
        if os.path.exists(r_dir):
            shutil.rmtree(r_dir)


if __name__ == '__main__':
    org = 'target_package'
    target = '{}_so'.format(org)
    main(project_dir=org, dst=target, remove=False)

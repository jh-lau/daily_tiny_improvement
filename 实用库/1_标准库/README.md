##[Python 标准库](https://docs.python.org/zh-cn/3/library/index.html)

### 1.文本处理服务
- [ ] string --- 常见的字符串操作
- [x] re --- 正则表达式操作
- [ ] difflib --- 计算差异的辅助工具
- [ ] textwrap --- 文本自动换行与填充
- [ ] unicodedata --- Unicode 数据库
- [ ] stringprep --- 因特网字符串预备
- [ ] readline --- GNU readline 接口
- [ ] rlcompleter --- GNU readline 的补全函数
    
### 2.二进制数据服务
- [ ] struct --- 将字节串解读为打包的二进制数据
- [ ] codecs --- 编解码器注册和相关基类

### 3.数据类型
- [ ] datetime --- 基本的日期和时间类型
- [ ] zoneinfo --- IANA 时区支持
- [ ] calendar --- 日历相关函数
- [x] collections --- 容器数据类型
    - namedtuple
    - defaultdict
- [ ] collections.abc --- 容器的抽象基类
- [x] heapq --- 堆队列算法
- [ ] bisect --- 数组二分查找算法
- [ ] array --- 高效的数值数组
- [ ] weakref --- 弱引用
- [x] types --- 动态类型创建和内置类型名称
- [ ] copy --- 浅层 (shallow) 和深层 (deep) 复制操作
- [ ] pprint --- 数据美化输出
- [ ] reprlib --- 另一种 repr() 实现
- [x] enum --- 对枚举的支持
- [ ] graphlib --- Functionality to operate with graph-like structures

### 4.数字和数学模块
- [ ] numbers --- 数字的抽象基类
- [ ] math --- 数学函数
- [ ] cmath --- 关于复数的数学函数
- [ ] decimal --- 十进制定点和浮点运算
- [ ] fractions --- 分数
- [x] random --- 生成伪随机数
- [ ] statistics --- 数学统计函数

### 5.函数式编程模块
- [x] itertools --- 为高效循环而创建迭代器的函数
    - chain
    - cycle
    - tee
    - repeat
    - zip_longest
    - islice
    - takewhile
    - dropwhile
    - filterfalse
    - product
    - permutations
    - combinations
- [x] functools --- 高阶函数和可调用对象上的操作
    - partial
- [ ] operator --- 标准运算符替代函数

### 6.文件和目录访问
- [ ] pathlib --- 面向对象的文件系统路径
- [ ] os.path --- 常用路径操作
- [ ] fileinput --- 迭代来自多个输入流的行
- [ ] stat --- 解析 stat() 结果
- [ ] filecmp --- 文件及目录的比较
- [ ] tempfile --- 生成临时文件和目录
- [x] glob --- Unix 风格路径名模式扩展
- [ ] fnmatch --- Unix 文件名模式匹配
- [ ] linecache --- 随机读写文本行
- [ ] shutil --- 高阶文件操作

### 7.数据持久化
- [ ] pickle --- Python 对象序列化
- [ ] copyreg --- 注册配合 pickle 模块使用的函数
- [ ] shelve --- Python 对象持久化
- [ ] marshal --- 内部 Python 对象序列化
- [ ] dbm --- Unix "数据库" 接口
- [ ] sqlite3 --- SQLite 数据库 DB-API 2.0 接口模块

### 8.数据压缩和存档
- [ ] zlib --- 与 gzip 兼容的压缩
- [ ] gzip --- 对 gzip 格式的支持
- [ ] bz2 --- 对 bzip2 压缩算法的支持
- [ ] lzma --- 用 LZMA 算法压缩
- [ ] zipfile --- 使用ZIP存档
- [ ] tarfile --- 读写tar归档文件

### 9.文件格式
- [ ] csv --- CSV 文件读写
- [ ] configparser --- 配置文件解析器
- [ ] netrc --- netrc 文件处理
- [ ] xdrlib --- 编码与解码 XDR 数据
- [ ] plistlib --- 生成与解析 Apple .plist 文件

### 10.加密服务
- [ ] hashlib --- 安全哈希与消息摘要
- [ ] hmac --- 基于密钥的消息验证
- [ ] secrets --- 生成安全随机数字用于管理密码

### 11.通用操作系统服务
- [ ] os --- 多种操作系统接口
- [ ] io --- 处理流的核心工具
- [ ] time --- 时间的访问和转换
- [x] argparse --- 命令行选项、参数和子命令解析器
- [ ] getopt --- C 风格的命令行选项解析器
- [x] logging --- Python 的日志记录工具
- [x] logging.config --- 日志记录配置
- [ ] logging.handlers --- 日志处理程序
- [ ] getpass --- 便携式密码输入工具
- [ ] curses --- 终端字符单元显示的处理
- [ ] curses.textpad --- 用于 curses 程序的文本输入控件
- [ ] curses.ascii --- 用于 ASCII 字符的工具
- [ ] curses.panel --- curses 的面板栈扩展
- [ ] platform --- 获取底层平台的标识数据
- [ ] errno --- 标准 errno 系统符号
- [ ] ctypes --- Python 的外部函数库

### 12.并发执行
- [x] threading --- 基于线程的并行
- [x] multiprocessing --- 基于进程的并行
- [ ] multiprocessing.shared_memory --- 可从进程直接访问的共享内存
- [x] concurrent 包
- [x] concurrent.futures --- 启动并行任务
- [x] subprocess --- 子进程管理
- [ ] sched --- 事件调度器
- [ ] queue --- 一个同步的队列类
- [ ] contextvars --- 上下文变量
- [ ] _thread --- 底层多线程 API

### 13.网络和进程间通信
- [ ] asyncio --- 异步 I/O
- [ ] socket --- 底层网络接口
- [ ] ssl --- 套接字对象的 TLS/SSL 包装器
- [ ] select --- 等待 I/O 完成
- [ ] selectors --- 高级 I/O 复用库
- [ ] asyncore --- 异步套接字处理器
- [ ] asynchat --- 异步套接字指令/响应处理程序
- [x] signal --- 设置异步事件处理程序
- [ ] mmap --- 内存映射文件支持

### 14.互联网数据处理
- [ ] email --- 电子邮件与 MIME 处理包
- [x] json --- JSON 编码和解码器
- [ ] mailcap --- Mailcap 文件处理
- [ ] mailbox --- 操作多种格式的邮箱
- [ ] mimetypes --- 映射文件夹到 MIME 类型
- [ ] base64 --- Base16, Base32, Base64, Base85 数据编码
- [ ] binhex --- 对binhex4文件进行编码和解码
- [ ] binascii --- 二进制和 ASCII 码互转
- [ ] quopri --- 编码与解码经过 MIME 转码的可打印数据
- [ ] uu --- 对 uuencode 文件进行编码与解码

### 15.结构化标记处理工具
- [ ] html --- 超文本标记语言支持
- [ ] html.parser --- 简单的 HTML 和 XHTML 解析器
- [ ] html.entities --- HTML 一般实体的定义
- [ ] XML处理模块
- [ ] xml.etree.ElementTree --- ElementTree XML API
- [ ] xml.dom --- The Document Object Model API
- [ ] xml.dom.minidom --- Minimal DOM implementation
- [ ] xml.dom.pulldom --- Support for building partial DOM trees
- [ ] xml.sax --- Support for SAX2 parsers
- [ ] xml.sax.handler --- Base classes for SAX handlers
- [ ] xml.sax.saxutils --- SAX 工具集
- [ ] xml.sax.xmlreader --- Interface for XML parsers
- [ ] xml.parsers.expat --- Fast XML parsing using Expat

### 16.互联网协议和支持
- [ ] webbrowser --- 方便的Web浏览器控制器
- [ ] cgi --- Common Gateway Interface support
- [ ] cgitb --- 用于 CGI 脚本的回溯管理器
- [ ] wsgiref --- WSGI Utilities and Reference Implementation
- [ ] urllib --- URL 处理模块
- [ ] urllib.request --- 用于打开 URL 的可扩展库
- [ ] urllib.response --- urllib 使用的 Response 类
- [ ] urllib.parse 用于解析 URL
- [ ] urllib.error --- urllib.request 引发的异常类
- [ ] urllib.robotparser --- robots.txt 语法分析程序
- [ ] http --- HTTP 模块
- [ ] http.client --- HTTP 协议客户端
- [ ] ftplib --- FTP 协议客户端
- [ ] poplib --- POP3 协议客户端
- [ ] imaplib --- IMAP4 协议客户端
- [ ] nntplib --- NNTP protocol client
- [ ] smtplib ---SMTP协议客户端
- [ ] smtpd --- SMTP 服务器
- [ ] telnetlib --- Telnet client
- [ ] uuid --- UUID objects according to RFC 4122
- [ ] socketserver --- A framework for network servers
- [ ] http.server --- HTTP 服务器
- [ ] http.cookies --- HTTP状态管理
- [ ] http.cookiejar —— HTTP 客户端的 Cookie 处理
- [ ] xmlrpc --- XMLRPC 服务端与客户端模块
- [ ] xmlrpc.client --- XML-RPC client access
- [ ] xmlrpc.server --- Basic XML-RPC servers
- [ ] ipaddress --- IPv4/IPv6 操作库

### 17.多媒体服务
- [ ] audioop --- 处理原始音频数据
- [ ] aifc --- 读写 AIFF 和 AIFC 文件
- [ ] sunau --- 读写 Sun AU 文件
- [ ] wave --- 读写WAV格式文件
- [ ] chunk --- 读取 IFF 分块数据
- [ ] colorsys --- 颜色系统间的转换
- [ ] imghdr --- 推测图像类型
- [ ] sndhdr --- 推测声音文件的类型
- [ ] ossaudiodev --- Access to OSS-compatible audio devices

### 18.国际化
- [ ] gettext --- 多语种国际化服务
- [ ] locale --- 国际化服务

### 19.程序框架
- [ ] turtle --- 海龟绘图
- [ ] cmd --- 支持面向行的命令解释器
- [ ] shlex --- Simple lexical analysis

### 20.Tk图形用户界面(GUI)
- [ ] tkinter --- Tcl/Tk的Python接口
- [ ] tkinter.colorchooser --- 颜色选择对话框
- [ ] tkinter.font --- Tkinter 字体封装
- [ ] Tkinter 对话框
- [ ] tkinter.messagebox --- Tkinter 消息提示
- [ ] tkinter.scrolledtext --- 滚动文字控件
- [ ] tkinter.dnd --- 拖放操作支持
- [ ] tkinter.ttk --- Tk主题部件
- [ ] tkinter.tix --- Extension widgets for Tk

### 21.开发工具
- [ ] typing --- 类型提示支持
- [ ] pydoc --- 文档生成器和在线帮助系统
- [ ] Python Development Mode
- [ ] Effects of the Python Development Mode
- [ ] ResourceWarning Example
- [ ] Bad file descriptor error example
- [ ] doctest --- 测试交互性的Python示例
- [x] unittest --- 单元测试框架
- [ ] unittest.mock --- mock对象库
- [ ] unittest.mock 上手指南
- [ ] 2to3 - 自动将 Python 2 代码转为 Python 3 代码
- [ ] test --- Python回归测试包
- [ ] test.support --- Utilities for the Python test suite
- [ ] test.support.socket_helper --- Utilities for socket tests
- [ ] test.support.script_helper --- Utilities for the Python execution tests
- [ ] test.support.bytecode_helper --- Support tools for testing correct bytecode generation

### 22.调试和分析
- [ ] bdb --- Debugger framework
- [ ] faulthandler --- Dump the Python traceback
- [ ] pdb --- Python 的调试器
- [ ] Python Profilers 分析器
- [ ] timeit --- 测量小代码片段的执行时间
- [ ] trace --- 跟踪Python语句执行
- [ ] tracemalloc --- 跟踪内存分配

### 23.软件打包和分发
- [ ] distutils --- 构建和安装 Python 模块
- [ ] ensurepip --- Bootstrapping the pip installer
- [ ] venv --- 创建虚拟环境
- [ ] zipapp --- Manage executable Python zip archives

### 24.Python运行时服务
- [x] sys --- 系统相关的参数和函数
- [ ] sysconfig --- Provide access to Python's configuration information
- [ ] builtins --- 内建对象
- [ ] `__main__` --- 顶层脚本环境
- [ ] warnings --- Warning control
- [ ] dataclasses --- 数据类
- [x] contextlib --- 为 with语句上下文提供的工具
- [x] abc --- 抽象基类
- [x] atexit --- 退出处理器
- [x] traceback --- 打印或检索堆栈回溯
- [ ] `__future__` --- Future 语句定义
- [ ] gc --- 垃圾回收器接口
- [x] inspect --- 检查对象
- [ ] site —— 指定域的配置钩子

### 25.自定义 Python 解释器
- [ ] code --- 解释器基类
- [ ] codeop --- 编译Python代码

### 26.导入模块
- [ ] zipimport --- 从 Zip 存档中导入模块
- [ ] pkgutil --- 包扩展工具
- [ ] modulefinder --- 查找脚本使用的模块
- [ ] runpy --- Locating and executing Python modules
- [ ] importlib --- import 的实现
- [ ] Using importlib.metadata

### 27.Python 语言服务
- [ ] parser --- 访问 Python 解析树
- [ ] ast --- 抽象语法树
- [ ] symtable --- Access to the compiler's symbol tables
- [ ] symbol --- 与 Python 解析树一起使用的常量
- [ ] token --- 与Python解析树一起使用的常量
- [x] keyword --- 检验Python关键字
- [ ] tokenize --- 对 Python 代码使用的标记解析器
- [ ] tabnanny --- 模糊缩进检测
- [ ] pyclbr --- Python 模块浏览器支持
- [ ] py_compile --- 编译 Python 源文件
- [ ] compileall --- Byte-compile Python libraries
- [ ] dis --- Python 字节码反汇编器
- [ ] pickletools --- pickle 开发者工具集

### 28.杂项服务
- [ ] formatter --- 通用格式化输出
- [ ] Windows系统相关模块
- [ ] msilib --- Read and write Microsoft Installer files
- [ ] msvcrt --- 来自 MS VC++ 运行时的有用例程
- [ ] winreg --- Windows 注册表访问
- [ ] winsound --- Sound-playing interface for Windows
- [ ] Unix 专有服务
- [ ] posix --- 最常见的 POSIX 系统调用
- [ ] pwd --- 用户密码数据库
- [ ] spwd --- The shadow password database
- [ ] grp --- 组数据库
- [ ] crypt --- Function to check Unix passwords
- [ ] termios --- POSIX 风格的 tty 控制
- [ ] tty --- 终端控制功能
- [ ] pty --- 伪终端工具
- [ ] fcntl --- The fcntl and ioctl system calls
- [ ] pipes --- 终端管道接口
- [ ] resource --- Resource usage information
- [ ] nis --- Sun 的 NIS (黄页) 接口
- [ ] Unix syslog 库例程
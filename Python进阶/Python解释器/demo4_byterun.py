"""
  @Author       : liujianhan
  @Date         : 2020/10/9 17:26
  @Project      : DailyTinyImprovement
  @FileName     : demo4_byterun.py
  @Description  : Byterun 中有 4 种主要的类型对象：
    VirtualMachine 类，管理最高层的结构，特别是调用栈，同时管理指令到操作的映射，是最开始写的 Python解释器 类的高级版本。
    Frame 类，每一个 Frame 对象都维护一个 code object 引用，并管理一些必要的状态信息，例如全局与局部的命名空间，以及对调用它自身的帧的引用和最后执行的字节码
    Function 类，我们实现 Function 来控制新的帧的创建。
    Block 类，一个只包装了三个属性的类，控制代码流程的时候会用到。
"""
import collections
import operator
import dis
import sys
import types
import inspect

Block = collections.namedtuple('Block', 'type, handler, stack_height')


class VirtualMachineError(Exception):
    pass


class VirtualMachine:
    """
    每次运行一个 Python 程序我们仅创建一个 VirtualMachine 对象，它维护一个调用栈、异常状态和帧之间传递的返回值。
    运行代码的入口是 run_code 方法，它读入 code object 并建立运行起第一个帧，之后会因为函数调用或其它原因在该帧之上建立新帧，
    直到最后第一个帧返回，代码运行结束
    """

    def __init__(self):
        # 调用栈
        self.frames = []
        # 当前运行的帧
        self.frame = None
        # frame返回时的返回值
        self.return_value = None
        self.lst_exception = None

    def run_code(self, code, global_names=None, local_names=None):
        frame = self.make_frame(code,
                                global_names=global_names,
                                local_names=local_names)
        self.run_frame(frame)

    def make_frame(self, code, callargs=None, global_names=None, local_names=None):
        """
        调用栈内帧的压入与弹出操作，创建帧的操作 make_frame（该方法的主要工作是对帧拥有的名字空间的初始化）
        :param code:
        :param callargs:
        :param global_names:
        :param local_names:
        :return:
        """
        if callargs is None:
            callargs = {}
        if global_names is not None:
            global_names = global_names
            if local_names is None:
                local_names = global_names
        elif self.frames:
            global_names = self.frame.global_names
            local_names = []
        else:
            global_names = local_names = {
                '__builtins__': __builtins__,
                '__name': '__main__',
                '__doc__': None,
                '__package__': None
            }
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)

        return frame

    def push_frame(self, frame):
        self.frames.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.frames.pop()
        if self.frames:
            self.frame = self.frames[-1]
        else:
            self.frame = None

    def run_frame(self, frame):
        """运行帧直至它返回"""
        self.push_frame(frame)
        while True:
            byte_name, arguments = self.parse_byte_and_args()
            why = self.dispatch(byte_name, arguments)
            while why and frame.block_stack:
                why = self.manage_block_stack(why)
            if why:
                break

        self.pop_frame()

        if why == 'exception':
            exc, val, tb = self.last_exception
            e = exc(val)
            e.__traceback__ = tb
            raise e

        return self.return_value

    def top(self):
        return self.frame.stack[-1]

    def pop(self):
        return self.frame.stack.pop()

    def push(self, *values):
        self.frame.stack.extend(values)

    def popn(self, n):
        if n:
            ret = self.frame.stack[-n:]
            self.frame.stack[-n:] = []
            return ret
        else:
            return []

    def parse_byte_and_args(self):
        """
        解析指令是否有参数，有则通过字节码参数得到方法参数，同时会更新当前帧的 last_instruction ，无参数指令占一字节，
        有参数指令占 3 个字节，其中参数占 2 个字节。不同指令的参数的意义不同，
        比如 POP_JUMP_IF_FALSE 的参数为跳转的目标位置，BUILD_LIST 的参数为列表中的元素数量，
        LOAD_CONST 的参数为实际方法参数在常量列表中的位置。
        :return:
        """
        f = self.frame
        opoffset = f.last_instruction
        byteCode = f.code_obj.co_code[opoffset]
        f.last_instruction += 1
        byte_name = dis.opname[byteCode]
        if byteCode >= dis.HAVE_ARGUMENT:
            arg = f.code_obj.co_code[f.last_instruction:f.last_instruction + 2]  # index into the bytecode
            f.last_instruction += 2  # advance the instruction pointer
            arg_val = arg[0] + (arg[1] << 8)
            if byteCode in dis.hasconst:  # Look up a constant
                arg = f.code_obj.co_consts[arg_val]
            elif byteCode in dis.hasname:  # Look up a name
                arg = f.code_obj.co_names[arg_val]
            elif byteCode in dis.haslocal:  # Look up a local name
                arg = f.code_obj.co_varnames[arg_val]
            elif byteCode in dis.hasjrel:  # Calculate a relative jump
                arg = f.last_instruction + arg_val
            else:
                arg = arg_val
            argument = [arg]
        else:
            argument = []

        return byte_name, argument

    def dispatch(self, byte_name, argument):
        why = None
        try:
            byte_code_fn = getattr(self, f"byte_{byte_name}", None)
            if byte_code_fn is None:
                if byte_name.startswith('UNARY_'):
                    self.unary_operator(byte_name[6:])
                elif byte_name.startswith('BINARY_'):
                    self.binary_operator(byte_name[7:])
                else:
                    raise VirtualMachineError(
                        f'unsupported bytecode type: {byte_name}'
                    )
            else:
                why = byte_code_fn(*argument)
        except:
            self.last_exception = sys.exc_info()[:2] + (None,)
            why = 'exception'

        return why

    def push_block(self, b_type, handler=None):
        stack_height = len(self.frame.stack)
        self.frame.block_stack.append(Block(b_type, handler, stack_height))

    def pop_block(self):
        return self.frame.block_stack.pop()

    def unwind_block(self, block):
        """Unwind the values on the data stack corresponding to a given block."""
        if block.type == 'except-handler':
            # The exception itself is on the stack as type, value, and traceback.
            offset = 3
        else:
            offset = 0

        while len(self.frame.stack) > block.stack_height + offset:
            self.pop()

        if block.type == 'except-handler':
            traceback, value, exctype = self.popn(3)
            self.last_exception = exctype, value, traceback

    def manage_block_stack(self, why):
        """管理一个 frame 的 block 栈
        在循环、异常处理、返回这几个方面操作 block 栈与数据栈
        """
        frame = self.frame
        block = frame.block_stack[-1]
        if block.type == 'loop' and why == 'continue':
            self.jump(self.return_value)
            why = None
            return why

        self.pop_block()
        self.unwind_block(block)

        if block.type == 'loop' and why == 'break':
            why = None
            self.jump(block.handler)
            return why

        if (block.type in ['setup-except', 'finally'] and why == 'exception'):
            self.push_block('except-handler')
            exctype, value, tb = self.last_exception
            self.push(tb, value, exctype)
            self.push(tb, value, exctype)  # yes, twice
            why = None
            self.jump(block.handler)
            return why

        elif block.type == 'finally':
            if why in ('return', 'continue'):
                self.push(self.return_value)

            self.push(why)

            why = None
            self.jump(block.handler)
            return why
        return why

    def byte_LOAD_CONST(self, const):
        self.push(const)

    def byte_POP_TOP(self):
        self.pop()

    ## Names
    def byte_LOAD_NAME(self, name):
        frame = self.frame
        if name in frame.f_locals:
            val = frame.f_locals[name]
        elif name in frame.f_globals:
            val = frame.f_globals[name]
        elif name in frame.f_builtins:
            val = frame.f_builtins[name]
        else:
            raise NameError("name '%s' is not defined" % name)
        self.push(val)

    def byte_STORE_NAME(self, name):
        self.frame.f_locals[name] = self.pop()

    def byte_LOAD_FAST(self, name):
        if name in self.frame.f_locals:
            val = self.frame.f_locals[name]
        else:
            raise UnboundLocalError(
                "local variable '%s' referenced before assignment" % name
            )
        self.push(val)

    def byte_STORE_FAST(self, name):
        self.frame.f_locals[name] = self.pop()

    def byte_LOAD_GLOBAL(self, name):
        f = self.frame
        if name in f.f_globals:
            val = f.f_globals[name]
        elif name in f.f_builtins:
            val = f.f_builtins[name]
        else:
            raise NameError("global name '%s' is not defined" % name)
        self.push(val)

    ## Operators
    UNARY_OPERATORS = {
        'POSITIVE': operator.pos,
        'NEGATIVE': operator.neg,
        'NOT':      operator.not_,
        'INVERT':   operator.invert,
    }

    def unary_operator(self, op):
        x = self.pop()
        self.push(self.UNARY_OPERATORS[op](x))

    BINARY_OPERATORS = {
        'POWER': pow,
        'MULTIPLY': operator.mul,
        'FLOOR_DIVIDE': operator.floordiv,
        'TRUE_DIVIDE': operator.truediv,
        'MODULO': operator.mod,
        'ADD': operator.add,
        'SUBTRACT': operator.sub,
        'SUBSCR': operator.getitem,
        'LSHIFT': operator.lshift,
        'RSHIFT': operator.rshift,
        'AND': operator.and_,
        'XOR': operator.xor,
        'OR': operator.or_,
    }

    def binary_operator(self, op):
        x, y = self.popn(2)
        self.push(self.BINARY_OPERATORS[op](x, y))

    COMPARE_OPERATORS = [
        operator.lt,
        operator.le,
        operator.eq,
        operator.ne,
        operator.gt,
        operator.ge,
        lambda x, y: x in y,
        lambda x, y: x not in y,
        lambda x, y: x is y,
        lambda x, y: x is not y,
        lambda x, y: issubclass(x, Exception) and issubclass(x, y),
    ]

    def byte_COMPARE_OP(self, opnum):
        x, y = self.popn(2)
        self.push(self.COMPARE_OPERATORS[opnum](x, y))

    ## Attributes and indexing

    def byte_LOAD_ATTR(self, attr):
        obj = self.pop()
        val = getattr(obj, attr)
        self.push(val)

    def byte_STORE_ATTR(self, name):
        val, obj = self.popn(2)
        setattr(obj, name, val)

    ## Building

    def byte_BUILD_LIST(self, count):
        elts = self.popn(count)
        self.push(elts)

    def byte_BUILD_MAP(self, size):
        self.push({})

    def byte_STORE_MAP(self):
        the_map, val, key = self.popn(3)
        the_map[key] = val
        self.push(the_map)

    def byte_LIST_APPEND(self, count):
        val = self.pop()
        the_list = self.frame.stack[-count]  # peek
        the_list.append(val)

    ## Jumps

    def byte_JUMP_FORWARD(self, jump):
        self.jump(jump)

    def byte_JUMP_ABSOLUTE(self, jump):
        self.jump(jump)

    def byte_POP_JUMP_IF_TRUE(self, jump):
        val = self.pop()
        if val:
            self.jump(jump)

    def byte_POP_JUMP_IF_FALSE(self, jump):
        val = self.pop()
        if not val:
            self.jump(jump)

    def jump(self, jump):
        self.frame.last_instruction = jump

    ## Blocks

    def byte_SETUP_LOOP(self, dest):
        self.push_block('loop', dest)

    def byte_GET_ITER(self):
        self.push(iter(self.pop()))

    def byte_FOR_ITER(self, jump):
        iterobj = self.top()
        try:
            v = next(iterobj)
            self.push(v)
        except StopIteration:
            self.pop()
            self.jump(jump)

    def byte_BREAK_LOOP(self):
        return 'break'

    def byte_POP_BLOCK(self):
        self.pop_block()

    ## Functions

    def byte_MAKE_FUNCTION(self, argc):
        name = None
        code = self.pop()
        defaults = self.popn(argc)
        globs = self.frame.f_globals
        fn = Function(name, code, globs, defaults, None, self)
        self.push(fn)

    def byte_CALL_FUNCTION(self, arg):
        lenKw, lenPos = divmod(arg, 256)  # KWargs not supported here
        posargs = self.popn(lenPos)

        func = self.pop()
        frame = self.frame
        retval = func(*posargs)
        self.push(retval)

    def byte_RETURN_VALUE(self):
        self.return_value = self.pop()
        return "return"

    ## Prints
    def byte_PRINT_ITEM(self):
        item = self.pop()
        sys.stdout.write(str(item))

    def byte_PRINT_NEWLINE(self):
        print("")


class Frame:
    """
    Frame 对象包括一个 code object 、局部和全局内置（builtin）的名字空间（namespace），对调用它的帧的引用，一个数据栈、
    一个 block 栈以及最后运行的指令的序号（在 code_obj 字节码中的位置）。由于 Python 在处理不同模块时对名字空间的处理方式可能不同，
    在处置内置名字空间时需要做一些额外的工作。
    """

    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.f_globals = global_names
        self.f_locals = local_names
        self.prev_fname = prev_frame
        # 数据栈
        self.stack = []
        # 块栈
        self.block_stack = []
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtins__']
            if hasattr(self.builtin_names, '__dict__'):
                self.builtin_names = self.builtin_names.__dict__
        # 最后运行的指令，初始为0
        self.last_instruction = 0


class Function:
    """
    Function 对象的实现有点复杂，而且它的实现细节对于我们理解解释器并不重要。我们唯一需要了解的就是每次调用一个函数其实就是调用了对象的
     __call__ 方法，每次调用都新创建了一个 Frame 对象并开始运行它。
    """
    __slots__ = [
        'func_code', 'func_name', 'func_defaults', 'func_globals',
        'func_locals', 'func_dict', 'func_closure',
        '__name__', '__dict__',
        '_vm', '_func',
    ]

    def __init__(self, name, code, globs, defaults, closure, vm):
        self._vm = vm
        self.func_code = code
        self.func_name = self.__name__ = name or code.co_name
        self.func_defaults = tuple(defaults)
        self.func_globals = globs
        self.func_locals = self._vm.frame.local_names
        self.__dict__ = {}
        self.func_closure = closure
        self.__doc__ = code.co_consts[0] if code.co_consts else None

        # Sometimes, we need a real Python function.  This is for that.
        kw = {
            'argdefs': self.func_defaults,
        }
        if closure:
            kw['closure'] = tuple(make_cell(0) for _ in closure)
        self._func = types.FunctionType(code, globs, **kw)

    def __call__(self, *args, **kwargs):
        callargs = inspect.getcallargs(self._func, *args, **kwargs)
        frame = self._vm.make_frame(
            self.func_code, callargs, self.func_globals, {}
        )
        return self._vm.run_frame(frame)


def make_cell(value):
    """创建一个真实的 cell 对象"""
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]


# class Block:
#     """
#     block 用于某些流控制，尤其是异常处理与循环。举个例子，在循环中，一个特殊的迭代器对象会存在于数据栈上直到循环结束才被弹出，
#     因此解释器必须跟踪什么时候循环继续，什么时候循环结束。我们创建 why 变量来标记流控制的状态，why 可能是 None 或者 continue 、
#     break 、exception 、return。通过 why 标记，我们才能确认如何操作 block 栈与数据栈。
#     假如 block 栈顶是一个循环 block ，why 的值为 continue ，那迭代器对象就需要继续保持在数据栈上，如果为 break ，则需要将迭代器对象弹出。
#     """
#     pass


if __name__ == '__main__':
    code = """
def loop():
    x = 1
    while x < 5:
        if x==3:
            break
        x = x + 1
        print(x)
    return x
loop()
        """
    # compile 能够将源代码编译成字节码
    code_obj = compile(code, "tmp", "exec")
    vm = VirtualMachine()
    vm.run_code(code_obj)

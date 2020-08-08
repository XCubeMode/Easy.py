# Author
# Cube_Mode
# Contact Me By Email
# 2807658845@qq.com
# Make Python More Easy
import time
import os


def p(index, e='\n', s=' ', f=False):
    '''
    Prints the index to a stream;
    \'e\' = end, string appended after the last value, default a newline;
    \'s\' = sep,  string inserted between values, default a space.
    \'f\'= flush, whether to forcibly flush the stream.
    Warning: \'p\' only provide basic print function,
    If you are going to develop a programm,\'p\' doesn't suggested.
    '''
    print(index, sep=s, end=e, flush=f)


def sleep(sec):
    '''
    A Time-Out, with out import time
    '''
    time.sleep(sec)


def turtle():
    '''
    Import the base of turtle
    '''
    import turtle
    return turtle.Turtle()


def o():
    def acc(p, m):
        '''
        os.access(path, mode).
        p -> path, m -> mode
        '''
        os.access(path=p, mode=m)
    def chd(p):
        '''
        os.chdir(path)
        p -> path
        '''
        os.chdir(path=p)
    def chf(p, f):
        '''
        os.chflag(path, flags)
        p -> path
        '''
    def pop(command, mode=''):
        '''
        Function same as os.popen()
        '''
        os.popen(command,mode)

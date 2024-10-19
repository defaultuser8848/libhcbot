from collections import namedtuple
from typing import Annotated,Union,Callable,NewType,Any

RawMessage=NewType("RawMessage",object)

class Handler():
    METHOD_WHISPER=0x1
    METHOD_CHAT=0x2
    HandlerProc=namedtuple("HandlerProc","methods func convert pre_check")
    def __init__(self):
        self._proclst=[]
    def parse_args(self,func):
        res={}
        for (k,v) in func.__annotations__.items():
            if v is RawMessage:
                res[k]=lambda x:x
        return res
    @staticmethod
    def _default_pre_check(msg:RawMessage):
        return True
    def register(self,
                 methods:int=METHOD_CHAT|METHOD_WHISPER,
                 pre_check=_default_pre_check
                 ):
        def _(func:Callable):
            args=self.parse_args(func)
            self._proclst.append(
                Handler.HandlerProc(methods,func,args,pre_check)
            )         
            return func
        return _
    def check(self,msg):
        t=()
        for i in self._proclst:
            t+=(i.pre_check(msg),)
        return t
    def handle(self,msg):
        for i in self._proclst:
            if i.pre_check(msg):
                kwargs={k:v(msg) for (k,v) in i.convert.items()}
                i.func(kwargs)

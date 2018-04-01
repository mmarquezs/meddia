import abc
import io
import typing

class Storage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fopen(path: str, mode: str) -> io.IOBase:
        pass
    def mkdir(path: str):
        pass
    def rmdir(path: str):
        pass
    def rm(path: str):
        pass
    def chmod(path: str):
        pass
    def chown(path: str):
        pass
    def walk(path: str) -> typing.Iterator:
        pass

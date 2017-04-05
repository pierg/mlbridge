from abc import ABCMeta, abstractmethod

class IWSCallback(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_open(self, ws):
        raise NotImplementedError()

    @abstractmethod
    def on_message(self, ws, message):
        raise NotImplementedError()

    @abstractmethod
    def on_error(self, ws, error):
        raise NotImplementedError()

    @abstractmethod
    def on_close(self, ws):
        raise NotImplementedError()
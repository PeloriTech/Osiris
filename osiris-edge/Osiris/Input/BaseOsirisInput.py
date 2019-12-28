from abc import ABC, abstractmethod


class BaseOsirisInput(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def is_opened(self) -> bool:
        pass

    @abstractmethod
    def release(self):
        pass

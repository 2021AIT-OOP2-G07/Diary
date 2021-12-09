from abc import ABC, abstractmethod
class AbstractDiary(ABC):
    @abstractmethod
    def get_dare(self):
        pass
    @abstractmethod
    def get_summary(self):
        pass
    @abstractmethod
    def get_author(self):
        pass

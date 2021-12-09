from abc import ABC, abstractclassmethod
class AbstractDiary(ABC):
    @abstractclassmethod
    def get_date(self):
        pass
    @abstractclassmethod
    def get_summary(self):
        pass
    @abstractclassmethod
    def get_author(self):
        pass
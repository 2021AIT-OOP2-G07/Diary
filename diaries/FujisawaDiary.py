from diaries.AbstractDiary import AbstractDiary


class FujisawaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "グループワーク初日楽しかった！"

    def get_author(self):
        return "Fujisawa"

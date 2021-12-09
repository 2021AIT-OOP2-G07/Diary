from diaries.AbstractDiary import AbstractDiary


class KamiyaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "今日は本格的にチームでの作業をした。難しかった。"

    def get_author(self):
        return "Kamiya"

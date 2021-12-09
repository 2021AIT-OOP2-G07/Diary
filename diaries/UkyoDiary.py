from AbstractDiary import AbstractDiary


class UkyoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return """今日は本格的にチームでの作業をした。訳が分からなかった。"""

    def get_author(self):
        return "Ukyo"